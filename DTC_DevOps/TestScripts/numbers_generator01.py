#! /usr/bin/env python3

"""Script to show generator example usage

Usage:
    python3 Generators
"""


#def square_numbers(numbers):

#this will generate an object but not put any numbers in memory
#    for n in numbers:
#        yield (n*n)    
    
#user_example = square_numbers([1,2,3,4,5,6,7,8,9,10])

#alternate method: List Comprehension
#user_example2 = [s*s for s in [1,2,3,4,5,6,7,8,9,10]]

#example generator by changing brackets
user_example2 = (s*s for s in [1,2,3,4,5,6,7,8,9,10])
#or
user_example3 = [n * 2 for n in range(10)]
# this will print the object created for each object, this will have to be done
# for each object called, very slow here

#print next(user_example)


# to print all objects created
#for digits in user_example:
#    print (digits)

#convert the for loop to a list
#note You can not directly call on list function in  IDLE
#print list(user_exmple)

print(next(user_example2)) #first object in list
print(user_example2) # object not in memory
print(user_example3) # list in memory



