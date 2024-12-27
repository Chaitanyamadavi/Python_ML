import numpy as np

#slicing numpy arrays

np1 =np.array([1,2,3,4,5,6,7,8,9])

#how to return [1,2,3,4,5]

print(np1[0:5])


#how to return from something to the end

print(np1[1:])

#how to return -ve slices

print(np1[-3:-1])

#steps

print(np1[0:5:2])

#Using steps for the entire array

print(np1[::2])

#slice a 2d array

np2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])

#how to pull an item out of an multidimensional array using numpy

print(np2[1,2])

#slicing in 2d array

print(np2[0:1, 1:3])

print(np2[0:2, 1:3])