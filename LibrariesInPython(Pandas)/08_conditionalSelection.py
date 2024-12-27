# < > = <= >= etc

import pandas as pd
import numpy as np

my_df= pd.read_csv('dog_data.csv')


#boolean
print(my_df == "BROWN")

#returns dataframe with data

print(my_df[my_df == "BROWN"])

#run them on a col

print(my_df[my_df == "BROWN"]["Color"])