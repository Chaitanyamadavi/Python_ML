
email = input("enter your email-")
if "@" in email:
        password = input("enter your password-")

        if email ==  "python@gmail" and password == "12345":
            print("hello user")
        elif email == "python@gmail" and password != "12345":
            print("incorrect password! try again")
            password = input("password-")
            if password == "12345":
                print("welcome user")
            else :
                print("wrong password, try again after 5 minutes!")
        else:
            print("fuck off")
else:
    print("imaginary email not found")
