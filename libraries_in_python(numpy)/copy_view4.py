import numpy as np

#copy vs view

np1 = np.array([1,2,3,4,5,6,7,8,9])

#create a view

np2 = np1.view()


print(f"original NP1 {np1}")
print(f"original NP2{np2}")

np1[0]= 55

print(f"Changed NP1 {np1}")
print(f"original NP2{np2}")


#create a copy
'''
np2 = np1.copy()
print(f"original NP1 {np1}")
print(f"original NP2{np2}")

np1[0]= 55

print(f"Changed NP1 {np1}")
print(f"original NP2{np2}")
'''