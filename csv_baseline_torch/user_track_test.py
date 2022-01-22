import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from model import *
from colorama import Fore
from metric import *
import pandas as pd

if __name__ == '__main__':
    track_df = pd.read_csv("./data/v1/user_track.csv")

    df = pd.read_csv("./data/v1/train.csv")
    max_id = 37045
    print(df.shape[0])
    start_count = []
    weekends_proportion = []

    for row in range(1, max_id+1):

        now_row = track_df.loc[track_df['id'] == row]
        start_times = now_row.shape[0]
        #ser = now_row['is_weekend']
        #ser.unique()
        #vc = ser.value_counts()[1]

        #weekend_times = ser.value_counts()[1]

        #weekend_proportion = weekend_times / start_times
        start_count.append(start_times)
        #weekends_proportion.append(weekend_proportion)

    df['start_count'] = pd.Series(start_count).values
   #df['weekends_proportion'] = pd.Series(weekends_proportion).values
    print(df)