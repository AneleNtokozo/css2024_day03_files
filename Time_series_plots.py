# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 11:34:38 2024

@author: AneleMahlangu
"""

import pandas 
import matplotlib.pyplot as plt

df = pandas.read_csv('data_02/time_series_data.csv', index_col=0)
#print(df.info())


# df['Date'] = pandas.to_datetime(df['Date'], format='%Y-%d-%m')

#print(df.info())
plt.plot(df['Date'], df['Temperature'])
