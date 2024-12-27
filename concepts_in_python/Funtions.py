def is_even(number):
    """ This function tells whether the given input is odd or even
    input - any valid integer
    output - odd/even
    created by- python coder
    last edited on- 2aug 2024
    """
    
    if number % 2 == 0:
        return("the given number is even")
    else:
        return("the given number is odd")
        
x= is_even(5)
print(x)


