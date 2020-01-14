#Lab 1 work

import math

def minor1(number):

    e = 0
    sigma = 0
    product = 1

    #1a - convergence

    e = (1+1/number)**number

    #1b - sigma notation
    
    for something in range(number+1):

        sigma += 5*(something**2)
    
        #print(sigma)

    #1c - profuct notation

    for somethingelse in range(1,number+1):

        product *= 3*(somethingelse**2)

        #print(product)

    return e, sigma, product

result = minor1(5)

print(result[0])

print(result[1])

print(result[2])

