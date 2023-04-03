#!python3

# Reciprocal
# have the program iterate through the list and determine the
# reciprocal of each number as a decimal and print it.
# use the try/except to find any invalid values and display
# the error message

#sample output:
"""
The reciprocal of 0 does not exist
The reciprocal of 1 is 1.0
The reciprocal of 2 is 0.5
The reciprocal of 3 is 0.3333333333333333
The reciprocal of 4 is 0.25
"""

numbers = [0,1,2,3,4]
for x in numbers:
    try:
        w = 1 / x
        print(f"the reciprocal of {x} is {w}")
    except Exception as e: 
        print(f"There was an error: {e}")