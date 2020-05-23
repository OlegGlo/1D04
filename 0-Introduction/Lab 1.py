#Lab 1 work

'''
Exponents

For loops 

range() function

For loop as sigma notation

functions
'''

import math

def minor1(number):

    e = 0
    sigma = 0
    product = 0

    #1a - convergence

    e = (1+1/number)**number
    #print(e)

    #1b - sigma notation
    
    for something in range(number+1):

        sigma += 5*(something**2)
    
        #print(sigma)

    #1c - profuct notation

    product = 3*1**2

    for somethingelse in range(2,number+1):

        product *= 3*(somethingelse**2)

        #print(product)

    return e, sigma, product

result = minor1(5)

print(result[0])

print(result[1])

print(result[2])

