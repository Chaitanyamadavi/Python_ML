import pandas as pd
import numpy as np

stuff = {
    'Corporation':['Apple', 'Google', 'Meta', 'Apple', 'Google','Meta'],
    'Employees':['John', 'April', 'Wes', 'Beth', 'Justin', 'Steph'],
    'Salary':[200, 220, 190, 130, 120, 150]}
# Create Dataframe
my_df = pd.DataFrame(stuff)
print(my_df)


#Group by corporation - to get object location in memory

company = my_df.groupby('Corporation')
print(company)

#sum

print(company.sum())

#mean- pandas can only perform mean function a varible like salary, it cannot perform it on company or 
 #print(company.mean())
 
#max/min
print(company.max())

#standard deviation

"""print(company.std())"""

#variance

"""print(company.var())"""

#Count

print(company.count())

#Describe

print(company.describe())

