import pandas as pd
import numpy as np

my_df= pd.read_csv('dog_data.csv')

#multiple conditional &

print(my_df[(my_df["Color"]== "BROWN") & (my_df["Breed"]=="MIXED")])

#get length
print(len(my_df[(my_df["Color"]== "BROWN") & (my_df["Breed"]=="MIXED")]))

#multiple conditionals or

print(my_df[(my_df["Color"]== "BROWN") | (my_df["Breed"]=="MIXED")])

#return specific column
#my_df[(my_df["Color"]== "BROWN") & (my_df["Breed"]=="MIXED")][ColumnName]

print(my_df[(my_df["Color"]== "BROWN") & (my_df["Breed"]=="MIXED")]["DogName"])