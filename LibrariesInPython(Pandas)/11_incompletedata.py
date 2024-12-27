import pandas as pd
import numpy as np

#create dummy data

stuff = {"A":[1,2,3], "B":[4,np.nan,6], "C":[7,8,9], "D":[10,11,12]}
my_df = pd.DataFrame(stuff)
print(my_df)


#drop a row with null data

"""print(my_df.dropna())"""

#drop a column with null data

"""print(my_df.dropna(axis=1))"""

#more than one? set threshold

"""print(my_df.dropna(thresh=2, axis=1))"""

#replace things with fillna()

print(my_df.fillna(value="hello"))

#use math functions

print(my_df.fillna(value=my_df["B"].mean()))

#min/max

print(my_df.fillna(value=my_df["B"].min()))

print(my_df.fillna(value=my_df["B"].max()))