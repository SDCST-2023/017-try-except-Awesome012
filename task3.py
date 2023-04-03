#!python 3

# Square root of a number

# Have the user enter in a number.  Use a try-except to see if the input
# is a valid number.  Determine the square root and use a try-except to
# catch exceptions if the number can not be square rooted
# note: Use the math.sqrt() function to determine a square root
# rather than number**(0.5) as we need to catch complex numbers as
# exceptions

"""
Sample Output
Enter a number:x
That is not a valid number
There is no square root   
Enter a number:-1
There is no square root
Enter a number:3       
The square root of 3.0 is 1.7320508075688772
"""
import math

num = input("please input a number")
try:
    float(num)
except:
    print("that is not a number")
try: 
    square = math.sqrt(num)
    print(f"the square root of {num} is :{square}")
except:
    print("there is no square root")
print(num)
print(square)