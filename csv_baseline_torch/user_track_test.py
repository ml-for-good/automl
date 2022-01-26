import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from model import *
from colorama import Fore
from metric import *
import pandas as pd

if __name__ == '__main__':
    track_df = pd.read_csv("./data/user_track.csv")

    df = pd.read_csv("./data/train0.csv")
    max_id = 37045
    print(df.shape[0])
    start_count = []
    weekends_proportion = []

    for row in range(1, max_id+1):

        now_row = track_df.loc[track_df['id'] == row]
        start_times = now_row.shape[0]
        start_count.append(start_times)

    df['start_count'] = pd.Series(start_count).values
    print(df)