print("""
A palindromic number reads the same both ways.
The largest palindrome made from the product
of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made
from the product of two 3-digit numbers.
""")

def is_palindrome (n):
    n = str(n)
    if list(n) == list(reversed(n)):
        return True
    else:
        return False

max_product = 0

for i in range(100, 999):
    for j in range(100, 999):
        if i*j > max_product:
            if is_palindrome(i*j) == True:
                max_product = i*j

print ('Largest palindrome made from the product of two 3-digit numbers:', max_product)
