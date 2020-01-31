
'''
72_base_10 calculations

while for loops

" end="" " in a print

fuck around with plots in pylab library

Some examples:
'''

import pylab
import math

def function1():
    values = list(range(10))

    values2 = []
    for index in values:
        values2.append(index**2)

    print(values)
    print(values2)

#function1()

def function2():
    floatlist = []
    element = -10.0
    step = 0.5

    for i in  range(41):
        floatlist.append(element)
        element = element + step

    print(floatlist)

function2()

def function3():
    x = floatlist
    y_cos = []
    y_tan = []

    for value in x:
        y_cos.append(math.cos(value))
        y_tan.append(math.tan(value))

    pylab.title("asa")
    pylab.plot(x,y_cos,"r--",x,y_tan,"y--")
    pylab.show()
    







