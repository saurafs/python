# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 20:20:07 2026

@author: Saurabh
"""

# import pandas as pd

# car = pd.Series(["Maruti","Honda","Suzuki","Toyota"])
# print(car)
# print(car[1])

#-----------------------------------------------------

# a=pd.Series(["apple","banana","gavava","grape"])
# a.index = a.index + 1
# print(a)   

#----------------------------------------------------

# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }

# myvar = pd.DataFrame(data)

# print(myvar)

#IMPORTING CSV AND COVERTING TO DATA FRAME------------

# car_data = pd.read_csv("car-sales.csv")
# print(car_data)

# exporting data to csv--------------------------------

# car_data.to_csv("car-sale-export.csv")

# ATTRIBUTE-------------------------------------------

# print(car_data.index)
# print(car_data.describe())
# print(car_data.info())
# print(car_data["Doors"].mean()) 
# print(car_data["Doors"].var()) 
# print(car_data["Doors"].std()) 
# print(len(car_data))

#SELECTING AND VIEWING OUR DATA----------------------

# print(car_data.head(5))
# print(car_data.tail(5))
# print(car_data)
# print(car_data[car_data["Make"]=="Toyota"])

#CROSSTAB--------------------------------------------

# print(pd.crosstab(car_data["Make"], car_data["Doors"])) 

#GROUPBY----------------------------------------------

# print(car_data.groupby(["Make"]).sum())

#PLOT HISTOGRAM---------------------------------------

# print(car_data.plot())
# print(car_data.hist())

#MANIPULATIND DATA USING PANDAS----------------------

# car_missing_data = pd.read_csv("car-sales-missing-data.csv")
# print(car_missing_data)

# car_missing_data = car_missing_data["Odometer"].fillna(#THE VALUE)
# car_missing_data["Odometer"].fillna(#THE VALUE, inplace = True)
# car_missing_data.dropna(#inplace = true)
# cardropna = car_missing_data.dropna()
# cardropna.to_csv("cardropnafile.csv")

#ADDING COLOUM TO DATAFRAME---------------------------

# seats_column = pd.serie([5,5,5,5,5]) 
# car_data["Number of Seats"] = seats_column

#ADDING COLOUM TO DATAFRAME using LIST---------------

# milage = [1,2,3,4,5,6,7,8,9,10]
# car_data["Milage of car"] = milage  HERE WE HAVE TO GIVE EXACT NUMBER OF VALUE TO LENGHT OF DATAFRAME

#APPLY FUNCTION--------------------------------------
# car_data["Odometer (KM)"] = car_data["Odometer (KM)"].apply(lambda x : x/1.6)
