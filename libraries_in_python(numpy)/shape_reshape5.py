import numpy as np

# Create 1d numpy array and Get shape
np1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(np1.shape)


#Create 2d numpy array and Get shape(rows/columns)
np2 = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
print(np2.shape)


#reshape 2d 
np3 = np1.reshape(3,4)
print(np3)


#reshape 3d
np4 = np1.reshape(3,2,2)
print(np4)


#Flatten to 1d

np5 = np4.reshape(-1)
print(np5)
print(np5.shape)