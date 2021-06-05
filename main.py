from math import nan
from os import name
from Station import station
import numpy as np
import datetime
import pandas as pd
from Map import map
from Point import point


# xoa du lieu nan trong du lieu NO2 mat dat trong file data.csv
df = pd.read_csv('data.csv')

romoveNanData = df.dropna(subset = ['NO2'])

romoveNanData.to_csv('data.csv', index = False, header=True)

