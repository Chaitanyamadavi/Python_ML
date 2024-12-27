import pandas as pd
import numpy as np
from numpy.random import rand

#Create a dataframe 

my_data = rand(4,3) #rows , columns
my_rows = ["A", "B", "C", "D"]
my_column = ["monday", "tuesday", "wednesday"]

my_df = pd.DataFrame(my_data , my_rows , my_column)
print(my_df) 

#import a CSV file (comma separated value)

my_df2 = pd.read_csv('dog_data.csv')
print(my_df2)

#how to access a particular row from a csv file

print(my_df2.loc[0])

#pullout multiple rows

print(my_df2.loc[[0,5]])