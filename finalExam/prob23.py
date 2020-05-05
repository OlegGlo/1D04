
def f1(x,y):
    return x+y

def f2(x,y,f):
    return f1(x,y)

def f3(x,y,f):
    return f(x,y,f)

print(f3(1,1,f2))