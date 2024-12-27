name = "naman"
age = 34

print("hello my name is " , name , " and i am ", age)
print("hello my name is %s and My age is %d" %(name, age))
print("hello my name is {} and my age is {}".format(name, age))

# there is a problem with these, when you use the first one , it's a bit tedious going in and out of string again and again.
# Second is the good one but we have a much better one, that is the third one.
#when you use the third one, the only problem we have is , when we have a lot of placeholders in the long string, it's gonna be a complete mess

print(f"hello my name is {name} and my age is {age}")
