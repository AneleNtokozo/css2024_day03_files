# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 11:49:15 2024

@author: AneleMahlangu
"""

# import pandas 
# import matplotlib.pyplot as plt

# # df = pandas.read_csv('chatfile.csv')
# df = pandas.read_csv('chatfile.csv', names = ["Time","NUN", "x", "y", "z"])
# df['Time'] = pandas.to_datetime(df['Time'], format = '%H:%M:%S').dt.time #we want to remove the date part so we can be left with time
# # print(df.info())

# plt.plot(df["Time"], df["x"],label = "x")
# plt.plot(df["Time"], df["x"],label = "y")
# plt.plot(df["Time"], df["x"],label = "z")

# df.plot(x ='Time', y = ['x', 'y',',z'])
####to help with viaualising the data
import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv('data_02/iris.csv')
profile = ProfileReport(df,title ="profiling Report")
profile.to_file("your_report.html")