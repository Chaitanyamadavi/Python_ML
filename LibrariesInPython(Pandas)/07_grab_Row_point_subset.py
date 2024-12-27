import numpy as np
import pandas as pd

my_df = pd.read_csv('temp.csv') 

#grab row

print(my_df.loc[2])

#grab row my index location

print(my_df.iloc[3])

#specific points my_df.loc[rows, column]

print(my_df.loc[1,"Color"])

#subset for grabbing multiple points at same time
# my_df.loc[[rows,rows],[column,column]]


print(my_df.loc[[1,2],["DogName","Breed"]])