import numpy as np
import pandas as pd

my_df = pd.read_csv('temp.csv')

#list approach

gender = ["male","female", "male", "female" ]
my_df["Gender"] = gender
print(my_df)

#add default values

my_df["alive/dead"] = [True]*len(my_df)
print(my_df)

#add nan value

my_df["show dog"] = [np.nan]*len(my_df)
print(my_df)

#add columns with insert()- allows position

my_df.insert(1,"adopted", [True]*len(my_df),True)
print(my_df)

#adding columm with assign method   

my_df2 = my_df.assign(Horse=[False]*len(my_df))
print(my_df2)