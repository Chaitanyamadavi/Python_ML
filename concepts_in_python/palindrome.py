def palin(text):
    if len(text)<= 1:
        print ("a palindrome")
    else:
        if text[0] == text[-1]:
            palin(text[1:-1])
        else:
            print("not a palindrome")

palin("malayalam")
palin("madam")
palin("python")