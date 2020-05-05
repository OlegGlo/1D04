
def Interesting_res(x):

    if x ** 2 <= 100:
        if x % 4 ==2:
            return "six"

        elif not x + 5 > 2:
            return x - 50
    
    else:
        if x < 0 and abs(x) > 3:
            return False

        else:
            return x / 10

print(Interesting_res(9.0))


