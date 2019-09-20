#! /usr/bin/env python3

"""Script to show generator performance 

Usage:
    python3 Generators 2
"""

#import mem_profile
import random
import time

students = ['Rick James','Martha Stewart','Billy Joel','Pepper Pots','Tony Stark','Cool Moe Dee','Kirmit the Frog','Jen Gelfling','Bob Ross','Prince']
classes = ['MATH','English','Science','Information Technology','Literature','Poetry','Cooking','Home Economics','Sports','Health']

#print ('Memory (Before): {}Mb'.format(mem_profile.memory_usage_resource()))

def student_list(num_students):
    result = []
    for  s in range(num_students):
        person = {
                'id': s,
                'name': random.choice(students),
                'major': random.choice(classes)
                }
        result.append(person)
    return result

def people_generator(num_students):
    for c in xrange(num_students):
        person = {
                'id': s,
                'name': random.choice(students),
                'major': random.choice(classes)
                    
                }
        yield person
t1 = time.clock()
student = student_list(1000000)
t2 = time.clock()


print('Time: {} Seconds'.format(t2-t1))




