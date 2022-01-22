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
    test_df = pd.read_csv("test_b.csv")
    a_df = pd.read_csv('all_info.csv')
    #start_count = []
    #weekends_proportion = []
    real_age = []
    user_setage = []
    gender = []
    playcard_level = []
    playcard_point = []
    playcard_coupon_num = []
    is_push_open = []
    utm_channel = []
    signup_day = []
    app_version = []
    manufacturer = []
    model = []
    add_all_num = []
    add_under_18_num = []
    add_under_30_num = []
    add_under_setage_num = []
    view_all_num = []
    view_under_18_num = []
    view_under_30_num = []
    view_under_setage_num = []
    msg_all_num = []
    msg_under_18_num = []
    msg_under_30_num = []
    msg_under_setage_num = []
    gift_all_num = []
    gift_under_18_num = []
    gift_under_30_num = []
    gift_under_setage_num = []
    max_cow = 456
    for i in range(1, max_cow):
        print(i)
        print(test_df.loc[i-1, 'id'])
        now = a_df.loc[test_df.loc[i-1, 'id']-1]
        print(now)

        #start_count.append(now['start_count'])
        #weekends_proportion.append(now['weekends_proportion'])
        real_age.append(now['real_age'])
        user_setage.append(now['user_setage'])
        gender.append(now['gender'])
        playcard_level.append(now['playcard_level'])
        playcard_point.append(now['playcard_point'])
        playcard_coupon_num.append(now['playcard_coupon_num'])
        is_push_open.append(now['is_push_open'])
        utm_channel.append(now['utm_channel'])
        signup_day.append(now['signup_day'])
        app_version.append(now['app_version'])
        manufacturer.append(now['manufacturer'])
        model.append(now['model'])
        add_all_num.append(now['add_all_num'])
        add_under_18_num.append(now['add_under_18_num'])
        add_under_30_num.append(now['add_under_30_num'])
        add_under_setage_num.append(now['add_under_setage_num'])
        view_all_num.append(now['view_all_num'])
        view_under_18_num.append(now['view_under_18_num'])
        view_under_30_num.append(now['view_under_30_num'])
        view_under_setage_num.append(now['view_under_setage_num'])
        msg_all_num.append(now['msg_all_num'])
        msg_under_18_num.append(now['msg_under_18_num'])
        msg_under_30_num.append(now['msg_under_30_num'])
        msg_under_setage_num.append(now['msg_under_setage_num'])
        gift_all_num.append(now['gift_all_num'])
        gift_under_18_num.append(now['gift_under_18_num'])
        gift_under_30_num.append(now['gift_under_30_num'])
        gift_under_setage_num.append(now['gift_under_setage_num'])

        #print(now['start_count'])
        print('\n')
    #start_count.append(0)
    #weekends_proportion.append(0)
    real_age.append(0)
    user_setage.append(0)
    gender.append(0)
    playcard_level.append(0)
    playcard_point.append(0)
    playcard_coupon_num.append(0)
    is_push_open.append(0)
    utm_channel.append(0)
    signup_day.append(0)
    app_version.append(0)
    manufacturer.append(0)
    model.append(0)
    add_all_num.append(0)
    add_under_18_num.append(0)
    add_under_30_num.append(0)
    add_under_setage_num.append(0)
    view_all_num.append(0)
    view_under_18_num.append(0)
    view_under_30_num.append(0)
    view_under_setage_num.append(0)
    msg_all_num.append(0)
    msg_under_18_num.append(0)
    msg_under_30_num.append(0)
    msg_under_setage_num.append(0)
    gift_all_num.append(0)
    gift_under_18_num.append(0)
    gift_under_30_num.append(0)
    gift_under_setage_num.append(0)
    #test_df['start_count'] = pd.Series(start_count).values
    #test_df['weekends_proportion'] = pd.Series(weekends_proportion).values
    test_df['real_age'] = pd.Series(real_age).values
    test_df['user_setage'] = pd.Series(user_setage).values
    test_df['gender'] = pd.Series(gender).values
    test_df['playcard_level'] = pd.Series(playcard_level).values
    test_df['playcard_point'] = pd.Series(playcard_point).values
    test_df['playcard_coupon_num'] = pd.Series(playcard_coupon_num).values
    test_df['is_push_open'] = pd.Series(is_push_open).values
    test_df['utm_channel'] = pd.Series(utm_channel).values
    test_df['signup_day'] = pd.Series(signup_day).values
    test_df['app_version'] = pd.Series(app_version).values
    test_df['manufacturer'] = pd.Series(manufacturer).values
    test_df['model'] = pd.Series(model).values
    test_df['add_all_num'] = pd.Series(add_all_num).values
    test_df['add_under_18_num'] = pd.Series(add_under_18_num).values
    test_df['add_under_30_num'] = pd.Series(add_under_30_num).values
    test_df['add_under_setage_num'] = pd.Series(add_under_setage_num).values
    test_df['view_all_num'] = pd.Series(view_all_num).values
    test_df['view_under_18_num'] = pd.Series(view_under_18_num).values
    test_df['view_under_30_num'] = pd.Series(view_under_30_num).values
    test_df['view_under_setage_num'] = pd.Series(view_under_setage_num).values
    test_df['msg_all_num'] = pd.Series(msg_all_num).values
    test_df['msg_under_18_num'] = pd.Series(msg_under_18_num).values
    test_df['msg_under_30_num'] = pd.Series(msg_under_30_num).values
    test_df['msg_under_setage_num'] = pd.Series(msg_under_setage_num).values
    test_df['gift_all_num'] = pd.Series(gift_all_num).values
    test_df['gift_under_18_num'] = pd.Series(gift_under_18_num).values
    test_df['gift_under_30_num'] = pd.Series(gift_under_30_num).values
    test_df['gift_under_setage_num'] = pd.Series(gift_under_setage_num).values

    test_df.to_csv('new_test_b.csv', index=0, encoding='utf_8')

if __name__ == '__main__':
    #add_track()
    #divide()
    add_test()