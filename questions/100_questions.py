#User will input (3ages).Find the oldest one

"""class Solution:
    def Age(self,x,y,z):
        if x==y==z:
            print("they all are of the same age")
        elif x>y and x>z:
            print("x is the oldest one")
        elif y>x and y>z:
            print("y is the oldest one")
        elif z>x and z>y:
            print("z is the oldest one")
            
obj = Solution()
obj.Age(1,48,98)"""

#Write a program that will convert celsius value to fahrenheit

"""class Solution():
    def Degree(self,x):      #Celsius = x, fahrenheit = y
        y = x * 1.8 +32
        print(y)

obj = Solution()
obj.Degree(38)"""

#User will input (2numbers).Write a program to swap the numbers

"""class Solution():
    def Numbers(self, x,y):
        temp = x
        x = y
        y = temp
        print(x)
        print(y)
        
obj = Solution() 
obj.Numbers(5,10)  """

#Write a program that will give you the sum of 3 digits

"""class Solution():
    def numbers(self, x:int , y:int, z:int):
        print(x+y+z)

obj= Solution()
obj.numbers(5,67,89)"""

#Write a program that will reverse a four digit number.Also it checks whether the reverse is true.

class Solution():
    def fourDigitNumber(self, x):
        