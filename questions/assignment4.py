#remove the multiple times occuring digits from the list

L1 = [1,1,2,3,4,5,5,6,6]
L = []

for i in L1:
    if i not in L:
        L.append(i)
        print(L)