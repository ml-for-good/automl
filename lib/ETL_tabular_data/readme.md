#Module Tabular-Data-ETL

This is an independent module for preprocessing tabular data(original file -> ready-to-train data). The goal is to **automatically** process the **continuous and categorical variables**( number and category).

##Dependency Library:
* import **pandas** as pd
* import **numpy** as np
* from **scipy.stats** import ks_2samp
* from **scipy.interpolate** import CubicSpline
* from **sklearn.ensemble** import RandomForestClassifier


##CAN DO
###1. Load data from single local file to memery -- Class Readfile
   * Controlled by the input Json 
   * Available **Read** File Types: .csv .xlsx .pkl
   * Available Data Types: number, category, **string**

###2. Data preprocessing automatically -- Class Structured_data_preprocess
   * Available Data Types: number, category, ~~**string**~~
   * Transfer labels(Y) to number
   * Detect categorical variables(X) and transfer them to numbers
   * Fillna (Method: Cubic spline interpolation and Median)
   * Error value correction e.g. _"1,3600"->13600_ OR _"1,3600.20m"->13600.20_ OR _"abc"->0_
   * Data normalization(Z-socre)
   
###3. Export modified data -- Class Structured_data_preprocess
   * Available **Export** File Types: .csv .xlsx .pkl

##Steps
* As like the test case "test_case_excel_mixed" in './code/processing.py':  
1. **Step One**: Get the input json. 
```
json1 =  json.dumps({'encoding':'utf8',
                     'read_type':'excel',
                     'read_path':'../data/',
                     'read_filename':'Zircon composition database_mixed.xlsx',
                     'sheetname':'岩浆岩数据库',
                     'output_type':'excel',
                     'output_path':'../data/',
                     'output_filename':'output_case1.xlsx',
                     'y_column':'Rock Type',
                     'Datatype':'mixed'
                     })
```
2. **Step Two**: Load data from local file to dataframe. 
```
import json  
df_test_case1 = Readfile(json.loads(json1)).load_data().df
```
3. **Step Three**: Create an object with input values (dataframe from step two, json from step one).  
```
structured_data = Structured_data_preprocess(df_test_case1,
                                             json.loads(json1))
```
4. **Step Four**: Use the interface to complete the preprocessing.  
```
structured_data.preprocessing()
```
5. **Step Five**: Export the modified data to the local file. 
```
structured_data.export_df()
```
####Finished!
   
