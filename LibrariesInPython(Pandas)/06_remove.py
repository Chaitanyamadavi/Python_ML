import numpy as np
import pandas as pd

my_df = pd.read_csv('temp.csv')

gender = ["male","female", "male", "female" ]
my_df["Gender"] = gender


#remove column

my_df.drop("Gender", axis=1, inplace= True)
print(my_df)

#remove row

my_df.drop(2, axis=0, inplace=True)
print(my_df)