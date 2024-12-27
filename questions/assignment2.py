#assume that the title function doesn't exist, then how would you convert the following into a title form result.

x = "hello my name is python"
L =[]
print(x.split())
for i in x.split():
    print(i.capitalize())   
    L.append(i.capitalize())
    print(L)
    
print(" ".join(L))


