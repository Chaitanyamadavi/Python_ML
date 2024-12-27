


def return_sum(func,L):
    result = 0
    for i in L:
        if func(i):
            result = result+i
    return result

L = [11,14,21,23,56,78,45,29,28]

x = lambda x:x%2==0
y = lambda x:x%2!=0
z = lambda x:x%3 == 0

print(return_sum(x,L))
print(return_sum(y,L))
print(return_sum(z,L))
