# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 10:42:03 2024

@author: AneleMahlangu
"""

import pandas as pd
file = pd.read_csv('data_02/iris.csv')
print(file)
print(file.info())
print(file.describe())

##this code has iris in the "last column", so we want to remove it
file["class"] = file["class"].str.replace("Iris-", "")

import matplotlib.pyplot as plt
import seaborn as sns
sns.pairplot(file, hue = "class")
plt.show()
