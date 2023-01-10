#!/usr/bin/python3

import pandas as pd 

user_file_path = 'datasets/spotify_final_dataset'

user_data = pd.read_csv(user_file_path)

print(user_data.describe())
