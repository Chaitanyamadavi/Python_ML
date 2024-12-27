import numpy as np

#1-d
np1 = np.array([1,2,3,4,5,6,7,8,9])
for i in np1:
    print(i)


#2d array

np2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
for i in np2:
    #for rows
    #print(i)
    for y in i:
        print(y)
        
#3d array

np3 = np.array([[[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]]])

"""
for x in np3:
    print(x)
    for y in x:
        print(y)
        for i in y:
            print(i)
            """

#Use nditer()

for x in np.nditer(np3):
    print(x)
