import pandas as pd
import numpy as np

my_df = pd.read_csv("temp.csv")

#create new column

my_df["frame header"] = ["dog1", "dog2", "dog3","dog4"]
print(my_df)

#set index
my_df.set_index("frame header", inplace = True)
print(my_df)

#reset index

my_df.reset_index(inplace=True)
print(my_df)

#drop column

my_df.drop("frame header", inplace=True, axis=1)
print(my_df)



