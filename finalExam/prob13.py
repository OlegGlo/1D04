def sum (a,b):
    s = []
    for i in range(len(a)):
        s.append(a[i]+b[i])
    return s

def add(A,B):
    c = []
    for i in range(len(A)):
        c.append(sum(A[i],B[i]))

    return  c

A = [[2,1,3],[-1,2,0]]
B =  [[1,1,-1],[2,0,6]]

print(add(A,B))

