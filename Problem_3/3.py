print ("""
Largest prime factor

Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

"""
)

import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def is_factor(i,n):
    if n%i == 0:
        return True
    return False

n = 600851475143
max_prime_factor = 0
primes = []
counter = 0
while counter < round(math.sqrt(n)):
    if is_prime(counter) == True:
        if is_factor(counter,n) == True:
            max_prime_factor = counter
    counter += 1
print ("The maximum prime factor is:", max_prime_factor)
