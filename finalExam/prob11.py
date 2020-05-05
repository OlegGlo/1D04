def conv(s,b):
    n = len(s)
    d = 1
    f = 0
    for i in range(n):
        f = f + int(s[n-i-1])*d
        d = d * b

    return f

print(conv("1111",2))