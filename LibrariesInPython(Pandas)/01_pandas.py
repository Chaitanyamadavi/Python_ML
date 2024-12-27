import pandas as pd

#panda series - It's like a table column - a 1 dimensional array holding any type of data

my_series = [4,5,6,7]
my_var = pd.Series(my_series)
print(my_var)
 
print(my_var[2])

#labels using index argument

my_index = ['a','b','c','d']
my_var2 = pd.Series(my_series,my_index)
print(my_var2)

cars = {"rolls royce":1 , "Mercedes":2, "land rover":4}
my_var3 = pd.Series(cars)
print(my_var3)