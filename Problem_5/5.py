print ("""
2520 is the smallest number that can be divided by
each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that
is evenly divisible by all of the numbers from 1 to 20?
 """)

def is_evenly_divisible(n):
    for i in range(1,20):
        if n%i != 0:
            return False
    return True

flag = 0
counter = 0
while flag == 0:
    counter += 20
    if is_evenly_divisible(counter) == True:
        print ("""the smallest positive number that
        is evenly divisible by all of the numbers from 1 to 20 is:""", counter)
        flag = 1
