
import math

def Calculation(R,r):
    A = 0

    A = 4*(math.pi**2)*R*r

    B = 4*(math.pi**2)*R*r*3

    C = 100*(abs(A-B)/B)

    return A,B,C
 
R_value = 5
r_value = 4

ans = Calculation(R_value,r_value)

print(ans[0])
print(ans[1])
print(ans[2])
