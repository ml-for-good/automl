import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from colorama import Fore


def divide(): #划分函数6 ： 2
    df = pd.read_csv('a.csv', encoding='utf-8')
    # df.drop_duplicates(keep='first', inplace=True)  # 去重，只保留第一次出现的样本
    df = df.sample(frac=1.0)  # 全部打乱
    cut_idx = int(round(0.25 * df.shape[0]))
    df_valid, df_train = df.iloc[:cut_idx], df.iloc[cut_idx:]
    df_valid.to_csv('a_valid.csv', index=0, encoding='utf_8')
    df_train.to_csv('a_train.csv', index=0, encoding='utf_8')

def add_track(): #加两项到track特征到all_info -> a.csv
    track_df = pd.read_csv("user_track.csv")

    df = pd.read_csv("all_info.csv")
    max_id = 37045
    #print(df.shape[0])
    start_count = []
    weekends_proportion = []

    for row in range(1, max_id + 1):
        print(row)
        now_row = track_df.loc[track_df['id'] == row]
        start_times = now_row.shape[0]
        ser = now_row['is_weekend']
        ser.unique()
        if len(ser.value_counts()) == 1:
            if ser.value_counts().index == 1:
                weekend_proportion = 1
            else:
                weekend_proportion = 0
        elif len(ser.value_counts()) == 0:
            weekend_proportion = 0
        else:
            vc = ser.value_counts()[1]
            weekend_times = ser.value_counts()[1]
            weekend_proportion = weekend_times / start_times

        start_count.append(start_times)
        weekends_proportion.append(weekend_proportion)

    df['start_count'] = pd.Series(start_count).values
    df['weekends_proportion'] = pd.Series(weekends_proportion).values
    # df['weekends_proportion'] = pd.Series(weekends_proportion).values
    df.to_csv('a.csv', index=0, encoding='utf_8')

def add_test(): #加两项特征到test
    test_df = pd.read_csv("test_a.csv")
    a_df = pd.read_csv('a.csv')
    start_count = []
    weekends_proportion = []
    max_cow = 365
    for i in range(1, max_cow):
        print(i)
        print(test_df.loc[i-1, 'id'])
        now = a_df.loc[test_df.loc[i-1, 'id']-1]

        start_count.append(now['start_count'])
        weekends_proportion.append(now['weekends_proportion'])
        print(now['start_count'])
        print('\n')
    start_count.append(0)
    weekends_proportion.append(0)
    test_df['start_count'] = pd.Series(start_count).values
    test_df['weekends_proportion'] = pd.Series(weekends_proportion).values
    test_df.to_csv('a_test.csv', index=0, encoding='utf_8')

if __name__ == '__main__':
    #add_track()
    divide()
    #add_test()