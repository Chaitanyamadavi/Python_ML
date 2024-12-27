import numpy as np

#array
np1= np.array([0,1,2,3,4,5,6,7,8,9])
print(np1)

#arange
np2 = np.arange(15)
print(np2)

#step
np3 =np.arange(0,10,2)
print(np3)

#zeros
np4 =np.zeros(12)
print(np4)
 
#multidimensional
np5 = np.zeros((2,10))
print(np5)

#full
np6 =np.full((10),5)
print(np6)

#multidimensional full
np7 =np.full((2,10),5)
print(np7)

#convert python list to numpy

my_list =[1,2,3,4,5]
np8 = np.array(my_list)
print(np8)