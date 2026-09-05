# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 15:56:22 2026

@author: Saurabh
"""

import pandas as pd
import numpy as np
import seaborn as sb

# print(sb.get_dataset_names()) # list of names of all built-in example datasets available in the library, 
# data=sb.load_dataset("titanic")
# print(data)

# sb.countplot(data, x="sex")

#-----------------------------------------------------------------------

# data1=sb.load_dataset("exercise")
# sb.histplot(data1,x="pulse", fill=True ,color='red')
# sb.boxplot(data1, x="pulse")
# sb.boxenplot(data1, x="pulse", color='red')
# sb.kdeplot(data1, x="pulse", hue='diet', fill=False , color='red'),sb.rugplot(data1, x="pulse", hue='diet')

#-----------------------------------------------------------------------

# data2=sb.load_dataset("flights")
# sb.lineplot(data2, x="year", y="passengers")
# sb.pointplot(data2, x="year", y="passengers")
# sb.barplot(data2, x="year", y="passengers", color="green")

#-----------------------------------------------------------------------

data3=sb.load_dataset("diamonds")
data3_sample = data3.sample(1000)
# sb.scatterplot(data3_sample, x='carat', y='price', marker = '+')
# sb.kdeplot(data3_sample, x='carat', y='price', fill=True, cmap='viridis')
# sb.relplot(data3_sample, x='carat', y='price', col='cut')
# sb.pairplot(data3_sample)
