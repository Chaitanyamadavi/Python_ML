#grab the first 5 rows
import numpy as np
import pandas as pd

my_df = pd.read_csv('dog_data.csv')

#grab from top using .head()

print(my_df.head())

print(my_df.head(6))

#grab from bottom using .tail()

print(my_df.tail())

print(my_df.tail(8))

#info
print(my_df.info())

#shape of rows and column

print(my_df.shape)

#get the no of dimension

print(my_df.ndim)

#get the datatype of column

print(my_df.dtypes)

#get statistics about the function

print(my_df.describe())

#describe a specific column

print(my_df['Breed'].describe())

#select specific columns using brackets

print(my_df['DogName'])

print(my_df.DogName)

#select specific columns using location

print(my_df.iloc[:,0])