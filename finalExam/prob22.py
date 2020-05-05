
def myst(n1,n2):
    g = 1
    k = 2
    while k <= n1 and k <= n2:
        if n1 % k == 0 and n2 % k== 0:
            g = k
        
        k+= 1

    return g

print(myst(4,12))

