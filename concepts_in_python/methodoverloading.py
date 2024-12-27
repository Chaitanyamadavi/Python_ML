class Geometry:
    
    def area (self,a,b=0):
        if b == 0:
            print(3.14*a*a)
        else:
            print(a*b)

obj = Geometry()
obj.area(4,5)
obj.area(1)