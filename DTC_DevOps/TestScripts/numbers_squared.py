#! /usr/bin/env python3

"""Script to show generator example usage

Usage:
    python3 Generators
"""


def square_numbers(numbers):
    result = []
    for n in numbers:
        result.append(n*n)
    return result
user_example = square_numbers([1,2,3,4,5,6,7,8,9,10])

#alternate method
#user_example2 = [s*s for s in [1,2,3,4,5,6,7,8,9,10]]    
    
    
print user_example
   