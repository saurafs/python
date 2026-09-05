# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 20:44:08 2026

@author: Saurabh
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# print(plt.plot())
# print(plt.show())

#STATELESS-----------------------------------------

# x=[1,2,3,4,5]
# y=[11,22,33,44,55]
# print(plt.plot(x,y))

#EXPLICIT------------------------------------------

# fig, ax = plt.subplots()
# ax.plot(x,[50,100,300,500])
 
#--------------------------------------------------

# fig, ax = plt.subplots(figsize = (10,10))
# ax.plot(x,y) 
# ax.set(title="simplePlot" ,xlabel ="x-axis", ylabel="y-axis")
# fig.savefig("plot.png")

#CREATING DATA---------------------------------------

y=[1,2,3,4,5,6,7,8,9,10]
np.random.seed(42)
x=np.random.randint(0,25,10,int)

#LINE PLOT-----------------------------------------

# fig, ax=plt.subplots()
# ax.plot(x,y)

#SCATTER PLOT-------------------------------------

# fig, ax=plt.subplots()
# ax.scatter(x,y)

#BAR PLOT-----------------------------------------

# fig, ax=plt.subplots()
# ax.bar(x,y)

#HORIZONTAL BAR----------------------------------

# fig, ax=plt.subplots()
# ax.barh(x,y)

#HISTOGRAM---------------------------------------

# fig, ax=plt.subplots()
# ax.hist(x,y)

#SUBPLOT-----------------------------------------

# fig,((ax1,ax2),(ax3,ax4)) = plt.subplots(nrows=2,ncols=2,figsize=(10,5))
# ax1.plot(x,y)
# ax2.bar(x,y)
# ax3.scatter(x,y)
# ax4.hist(x,y)

#SUBPLOT 2----------------------------------------

# fig,((ax1,ax2),(ax3,ax4)) = plt.subplots(nrows=2,ncols=2,figsize=(10,5))
