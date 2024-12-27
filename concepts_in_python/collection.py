class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def intro(self):
        print("my name is", self.name ,"and I am", self.age)
c1= Customer("python", 82)
c2 = Customer("java", 67)
c3 = Customer("cPP", 28)

L= [c1,c2,c3]

for i in L:
    i.intro()