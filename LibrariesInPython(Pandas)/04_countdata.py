import numpy as np
import pandas as pd

my_df = pd.read_csv('dog_data.csv')

#Count distinct values -descending

print(my_df['Color'].value_counts())

#Count distinct values - ascending

print(my_df['Color'].value_counts(ascending=True))

#how to print Nan values

"""print(my_df["DogName"].value_counts(dropna=False))"""

#relative frequency - percentage

print(my_df['Color'].value_counts(normalize=True))

#get a specific Item count

print(my_df['Color'].value_counts()["WHITE"])


#count unique values - size 

print(my_df.groupby('Color').size())

#count unique values - count

print(my_df.groupby('Color').count())

#get a count of all columns across all columns

"""print(my_df.apply(pd.value_counts))"""