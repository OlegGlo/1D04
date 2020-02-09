
'''
fucntions (basic shit)

we can add lists (a + b)

global vs local variables



'''

x,y=10,20

def example(x):
    global y
    #print(x,y)
    y = y + 10

    print(x,y)
    return x

example(x)

print (x,y)

#this is global / local example^^^