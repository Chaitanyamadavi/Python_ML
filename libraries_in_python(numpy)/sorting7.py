import numpy as np

#np.sort() numerical

np1 = np.array([5,67,8,4,6,7,])
print(np.sort(np1))

 
#alphabetical

np2 = np.array(["John","Cena","Roman"])
print(np.sort(np2))

#booleans

np3 = np.array([True, False, False,True])
print(np.sort(np3))

#sorting is returning copies in the result""" without making any change in the original list

#2-d sort

np4 = np.array([[82,43,56,78],[11,2,333,9]])
print(np.sort(np4))