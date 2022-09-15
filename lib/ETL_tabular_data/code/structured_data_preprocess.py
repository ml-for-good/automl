
import re
import string
import json

import pandas as pd
import numpy as np

from scipy.stats import ks_2samp
from scipy.interpolate import CubicSpline

from sklearn.ensemble import RandomForestClassifier


# line 90, 92, 94 and 142 will cause the same warning, and the warning is as below
# 'D:\anaconda\lib\site-packages\pandas\core\indexing.py:1637: SettingWithCopyWarning:
#  A value is trying to be set on a copy of a slice from a DataFrame'
import warnings
warnings.filterwarnings("ignore")

class readfile:
    def __init__(self, json_ ):
        self.encoding = json_['encoding']  # just for the .csv file
        self.read_type = json_['read_type']  # available type: csv/ excel/ pickle
        self.read_path = json_['read_path']  # path of file which is about to load
        self.read_filename = json_['read_filename']  # filename of file which is about to load
        self.sheetname = json_['sheetname']  # just for the .xlsx file
        self.df = pd.DataFrame()  # 初始化dataframe

    def load_data(self): # load data from file
        if self.read_type == 'pickle'\
                and self.read_filename[-3:]=='pkl':
            self.df = pd.read_pickle(''.join([self.read_path, self.read_filename]))
            return self
        elif self.read_type == 'csv'\
                and self.read_filename[-3:]=='csv':
            try:
                self.df = pd.read_csv(''.join([self.read_path,self.read_filename]),
                                      encoding=self.encoding)
            except:
                raise "lost filepath,filename or encoding."
            return self
        elif self.read_type == 'excel'\
                and (self.read_filename[-4:] == 'xlsx' or self.read_filename[-4:] == 'xls'):
            try:
                self.df = pd.read_excel(''.join([self.read_path,self.read_filename]),
                                        sheet_name=self.sheetname)
            except:
                raise "lost filepath,filename or sheetname."
            return self
        # did not load file
        raise Exception("Invalid file type, please transfer the file into a .pkl, .csv or .xlsx file, and try again.")

class Structured_data_preprocess:

    def __init__(self, origin_dataframe,json_):
        self.df = origin_dataframe
        self.y_column = json_['y_column']  # the column name of y
        self.flag = json_['Datatype']  # tabular table type : number / mixed (number + category)
        self.output_type = json_['output_type']  # csv/excel/pickle
        self.output_path = json_['output_path']
        self.output_filename = json_['output_filename']

    def get_column_name(self):  # to get the names of columns in dataframe
        return self.df.columns.values

    def series_str2num(self,series):  # modify each column to make sure there is only computable numbers

        for tmp_n in range(series.shape[0]):
            try:
                # string -> number
                if type(series[tmp_n]) == str:
                    pattern = '[-+]?[0-9]+\.?[0-9]*'
                    try:
                        tmp_str = re.search(pattern, series[tmp_n]).group()
                    except:
                        tmp_str = ''

                    if tmp_str == '':
                        tmp_str_origin = series[tmp_n]
                        tmp_str_result = '0'
                        flag = False
                        for char in tmp_str_origin:
                            if char in string.digits:
                                flag = True
                                break
                        if flag ==True:
                            for char in tmp_str_origin:
                                if char == '.' or char in string.digits:
                                    tmp_str_result = ''.join([tmp_str_result, char])
                                series.iloc[tmp_n] = float(tmp_str_result)
                        else:
                            series.iloc[tmp_n] = np.nan
                    else:
                        series.iloc[tmp_n] = float(tmp_str)
                else:
                    continue
            except TypeError as t:
                print('------------ series_str2num -----------')
                raise Exception(series[tmp_n])
        return series

    def series_fillna(self, series, k=5):

        # Obtain the interval of interpolation samples
        def cal_interval(s, n, k=k):
            up_index = list(range(n - k, n))
            down_index = list(range(n + 1, n + 1 + k))
            if n + 1 + k > series.shape[0]:
                down_index = [_ - series.shape[0] for _ in down_index]  # 防止结尾越界
            y = s.iloc[up_index + down_index]  # 取数
            y = y[y.notnull()]  # Remove all null values
            return y

        # Cubic spline interpolation
        def ployinterp_column_CubicSpline(s, n, k = k):

            y = cal_interval(s, n, k)
            if len(y)< 2:
                return 0
            else:
                return CubicSpline(list(range(len(y))), list(y), bc_type='natural')(k)

        # Backup original series( Used to compare the distribution after interpolation)
        series = self.series_str2num(series)
        origin_series = series.copy(deep=True)
        notnull_series = series[series.notnull()]

        for i, index in enumerate(series[series.isnull() == True].index):

            import warnings
            warnings.filterwarnings("ignore")

            series.iloc[index] = float(ployinterp_column_CubicSpline(series, index))  # 返回当前数据的位置

        # After interpolation, check whether the distribution changes
        result = ks_2samp(list(notnull_series), list(series), alternative='two-sided', mode='auto')
        if result[1] >= 0.05:  # When the distribution is consistent, the interpolated series is returned
            return series
        else:  # 当分布完全改变时，回退fillna操作 并用非空数集合的中位数fillna.
               # When the distribution was completely changed, back off and fill the blank with the median
            origin_series = origin_series.fillna(notnull_series.median())
            return origin_series

    # the entrance to fillna each column
    def df_fillna(self,column):
        self.df[column] =  self.series_fillna(self.df[column])

    # To check whether the column is about category or not
    def check_category(self,series):
        def IsChinese(character):
            '''判断是否为中文字符'''
            for cha in character:
                if  '\u0e00' <= cha <= '\u9fa5':
                    return True
            else:
                return False
        def IsEnglish(character):
            '''判断是否为英文字母'''
            for cha in character:
                if  'A' <= cha <= 'Z' or  'a' <= cha <= 'z':
                    return True
            else:
                return False
        new_series = series[:min(len(series), 100)]
        count = 0
        for item in new_series:
            if type(item) != str and np.isnan(item)==False:  # 列数据的类型是int/float，且不是空值
                return False
            if type(item) == str and (IsChinese(item)==True or IsEnglish(item) == True):  # 列数据类型是string,且包含中英文字符
                count += 1
                if count >= 2:
                    return True
        return False

    def processing_by_columns(self):
        columns = self.get_column_name()
        if self.flag == 'number':
            for item in columns:
                if item != self.y_column:
                    self.df_fillna(item)
            return self
        elif self.flag == 'mixed':
            for item in columns:
                if item != self.y_column:
                    # 判断是否是 分类变量列
                    if self.check_category(self.df[item]): # 是分类变量列 the column is about category
                         tmp_df = pd.get_dummies(self.df[item],prefix=item, prefix_sep='_', dummy_na=True)
                         self.df = self.df.drop(columns=[item],axis=1,inplace=False)
                         self.df = self.df.join(tmp_df)
                    else:  # 不是分类变量列,即连续变量列。 the column IS NOT about category, just numbers
                        self.df_fillna(item)
            return self
        else:
            raise Exception( " Wrong DataType, please select one from 'number/mixed' ")

    #transfer the label of y column to numbers
    def labal2num(self):
        set_name = set(self.df[self.y_column])
        d,n = {},0
        for item in set_name:
            d[item] = n
            n += 1
        print(str(d))
        self.df[self.y_column] = self.df[self.y_column].map(d)
        return self

    def get_df_shape(self):
        return self.df.shape  # tuple

    # Feather engineering by random forest
    # the feather will be appended automatically until the sum of R_Square > 0.8
    def feature_selection_RF(self):

        y = self.df[self.y_column]
        x = self.df.drop(self.y_column, axis=1)
        clf = RandomForestClassifier()
        clf.fit(x, y)
        importance = clf.feature_importances_
        indices = np.argsort(importance)[::-1]
        features = x.columns
        final_feature, sum_r2 = [], 0
        for f in range(x.shape[1]):
            final_feature.append(features[f])
            sum_r2 += importance[indices[f]]
            if sum_r2>0.8:
                break
        final_feature.append(self.y_column)
        self.df = self.df[final_feature]
        return self

    # using z-score to normalize the data
    def z_score(self):
        y = self.df[self.y_column]
        x = self.df.drop(self.y_column, axis=1)
        self.df = x.apply(lambda a: (a - a.mean()) / a.std())
        self.df[self.y_column] = y
        return self

    # the main function throughout the whole process
    def preprocessing(self):

        # 丢掉超过半数为空的列/行
        _index = self.get_df_shape()[1]//2
        self.df = self.df.dropna(how='all', axis=1)\
            .dropna(how='all', axis=0)\
            .dropna(thresh=_index)\
            .reset_index(drop=True)

        self.labal2num()
        self.processing_by_columns()  # number/mixed
        self.z_score()
        self.feature_selection_RF()
        return self # the dataframe has been finished ETL 已完成ETL，此时的self.df即为最后结果

    # export dataframe to prefered file type
    def export_df(self):
        if self.output_path[-1]!='/':
            self.output_path = ''.join([self.output_path, '/'])
        if self.output_type =='pickle' \
                and self.output_filename[-3:]=='pkl':
            self.df.to_pickle(''.join([self.output_path, self.output_filename]), index=False)

        elif self.output_type == 'csv' \
                and self.output_filename[-3:]=='csv':
            self.df.to_csv(''.join([self.output_path, self.output_filename]), index=False)

        elif self.output_type == 'excel' \
                and self.output_filename[-4:]=='xlsx':
            self.df.to_excel(''.join([self.output_path, self.output_filename]), index=False)

        else:
            raise Exception( "Wrong output file type, please select one from 'pickle/csv/excel'. ")


# test case One: excel file, purely number
def test_case_excel_number():
    # creating input string of json
    json1 =  json.dumps({'encoding':'utf8',
                         'read_type':'excel',
                         'read_path':'../data/',
                         'read_filename':'Zircon composition database_number.xlsx',
                         'sheetname':'岩浆岩数据库',
                         'output_type':'excel',
                         'output_path':'../data/',
                         'output_filename':'output_case1.xlsx',
                         'y_column':'Rock Type',
                         'Datatype':'number'
                         })
    #load file to dataframe
    df_test_case1 = readfile(json.loads(json1)).load_data().df
    # create the object
    structured_data = Structured_data_preprocess(df_test_case1,
                                                 json.loads(json1))
    # ETL processing for dataframe
    structured_data.preprocessing()
    #export the dataframe to different file
    structured_data.export_df()


# test case Two: excel file, mixed datatype
def test_case_excel_mixed():
    json2 =  json.dumps({'encoding':'utf8',
                         'read_type':'excel',
                         'read_path':'../data/',
                         'read_filename':'Zircon composition database_mixed.xlsx',
                         'sheetname':'岩浆岩数据库',
                         'output_type':'excel',
                         'output_path':'../data/',
                         'output_filename':'output_case_mixed.xlsx',
                         'y_column':'Rock Type',
                         'Datatype':'mixed'
                         })
    # load file to dataframe
    df_test_case2 = readfile(json.loads(json2)).load_data().df
    # ETL for loaded dataframe
    structured_data = Structured_data_preprocess(df_test_case2,
                                                 json.loads(json2))
    structured_data.preprocessing()
    structured_data.export_df()


# test case Three: exteranl json with customized needs
def test_case_external_json(_json):
    df_test_case2 = readfile(json.loads(_json)).load_data().df
    structured_data = Structured_data_preprocess(df_test_case2,
                                                 json.loads(_json))
    structured_data.preprocessing()
    structured_data.export_df()


# test_case_excel_number()
# test_case_excel_mixed()
