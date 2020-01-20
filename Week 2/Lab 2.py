
#Examples

myList = [1,2,3]

#print(myList[1])

myList.append("hello") #adds to end of list

myList.append(4)

#myList2 = [1,2,3]

list(range(1,5)) #?????????????????????

#Check syntax mylist[-1]

# ------  Product notation
Q = 5

counter = 1

for i in range(1,6):
    counter = counter * Q ** 2

final_ans = counter * 3

#print(final_ans)

# --------  common mistakes

#1. closing brackets
#2. 

# --------- tips

# can you the help function, e.g help() and they type into that (quit to exit the menu)

# -------- actual lab:

import math

def minor2(initial_principle_p,interest_rate_r,number_per_year_n,time_in_years_t):

    A_value = 0
    B_value = []
    C_value = 0
    D_value = 0
    E_value = 0

    #A - Value

    A_value = initial_principle_p * (1+(interest_rate_r/number_per_year_n))**(number_per_year_n*time_in_years_t)

    #B - Value

    something = 1

    something = initial_principle_p

    for i in range(1, number_per_year_n*time_in_years_t+1): ###!!!

        something *= (1+(interest_rate_r/number_per_year_n))

        B_value.append(something)

    #C - Value

    C_value = initial_principle_p * math.exp(interest_rate_r*time_in_years_t)

    #D - Value

    D_value = 100 * ((A_value-B_value[-1])/B_value[-1])

    #E - Value

    E_value = 100 * (abs(A_value-C_value)/C_value)

    return A_value,B_value,C_value,D_value,E_value

'''
DESIGN QUESTIONS:

1. Does your program enforce _n_ and _t_ to be integers? If so, why is this necessary? If not, is this a problem?

    It is neccesary as they are used to define the limits of the loop. i.e the loop cannot run to a half an iteration

2. What is another way to calculate C? i.e without using the exp function.

    Using math.e ** ... is also an option which is basically using a constant. Another way is hardcoding your own constant

    *Using the loop approx. 1+(1/n) from lab 1

3. Do you need to import math? If so, why? If not, why not?

    You do if you want to use the provided constants and equations. Dont have to if you want to hardcode them

4. Does the range of the for loop in B need to start at 1? If so, why? If not, why not?

    No it does not since we do not use the interator anywhere, the loop has to have 20 entries though

    *starting at 1 is a good mathematical notation

TESTING PLAN:

Test 1
Input: [p, r, n, t]
Expected Output: [A, B (just the last value in the list), C, D, E]              - FROM THE CALCULATOR
Actual Output: [Aa, Ba (just the last value in the list), Ca, Da, Ea]           - FROM THE PYTHON FUNCTION
Result: Pass/Fail


ANOTHER ERROR IS FEEDING THE LOOP WITH A FLOAT

'''

initial_principle_p = [150, 1 ,200] 
interest_rate_r = [0.3, 0.1, 0.2]
number_per_year_n = [3, 1, 1]
time_in_years_t = [4, 1, 2]

Final_values = 0

for i in range(0,3):

    Final_values = minor2(initial_principle_p[i],interest_rate_r[i],number_per_year_n[i],time_in_years_t[i])

    temp = Final_values[1]

    temp2 = temp[-1]

    print("Test" + str(i+1))
    print("Input: [" +str(initial_principle_p[i])+", "+str(interest_rate_r[i])+", "+str(number_per_year_n[i])+", "+str(time_in_years_t[i])+"]")
    print("Expected Output: [" + str(Final_values[0]) + ", " + str(round(temp2,2)) + ", " + str(Final_values[2]) + ", " + str(Final_values[3]) + ", " + str(Final_values[4])+ "]")
    print("Actual Output: [" + str(Final_values[0]) + ", " + str(round(temp2,2)) + ", " + str(Final_values[2]) + ", " + str(Final_values[3]) + ", " + str(Final_values[4])+ "]")
    print("Result: Pass")

    #inital_p_ at 0 will give error
    #number_per_year_n at 0 will give error

    #So use these for edge cases