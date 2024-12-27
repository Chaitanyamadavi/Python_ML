#techniques to measure time efficiency

#1) measuring time to execute

import time
start = time.time()

for i in range(0,101):
    print(i)
print(time.time()- start)

#counting operations

def c_to_f(c):
    return c*9/5 +32

obj = c_to_f(36)
print(obj)

#order of growth

def fact(n):
    answer = 0
    while n > 1:
        answer *= n
        n -= 1
    return answer

obj1 = fact(5)
print(obj1)