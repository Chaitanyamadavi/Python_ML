#problem 1

L = [1,2,3,4,5]

sum = 0
for i in L:
    sum = sum+ i
    print(sum)

product = 1
for x in L:
    product = product *x
    print(product)
    
#Answer - the complexity for this program is O(n)

#problem 2

L = [1,2,3,4,5]

for i in L:
    for j in L:
        print('({},{})'.format(i,j))
     
     
     
#problem 3 - linear search

#the order of complexity for linear search is O(n)

#problem 4

def InttoStr(i):
    digits= '0123456789'
    if i == 0:
        return '0'
    result = ''
    if i > 0:
        result = digits[i%10]+ result
        i = i//10
    return result

print(InttoStr(1230))

#Whenever the things are getting divided, remember that the complexity used is O(logn)

#problem 5

a = [1,2,3,4]
b = [2,3,4,5,6]

for i in a:
    for j in b:
        if i<j:
            print('({},{})'.format)

#the complexity for this program is O(ab), where a is the no of elements present is array "a" and same for b

# for recursion the complexity is linear so O(n)

#fibbonacci has a complexity of O(1.7^n)

#when their is no loop and no recursion in a program and it just has arithmetic operations the time complexity of the code is constant - O(1)

#problem 16

def sum_digits(num):
    sum = 0
    while(num>0):
        sum+=num%10
        num/=10
    return sum

print(sum_digits(45))


