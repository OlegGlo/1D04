

'''
Type conversions

x = 1

str(x)

difference between

if 
if

and 

if
elif



'''

def buzz(checkNum, buzzNum):

    splitted = str(checkNum)

    #print(int(splitted[1]))

    if checkNum == 0:

        return str(checkNum)

    else:

        if checkNum % buzzNum == 0:

            #print("Buzz")

            return "Buzz"

        elif str(checkNum).find(str(buzzNum)) >= 0:

            #print("Buzz")

            return "Buzz"

        else:

            stringconversion = str(checkNum)

            #print(stringconversion)

            return stringconversion


def whileBuzz(buzzCount, buzzNum):

    #buzzEnd = 1

    buzzTime = 0

    count = 0

    buzzCounter = 0

    buzzLoop = []

    #buzzNum = 0

    while buzzTime != buzzCount:

        x = buzz(count, buzzNum)

        if x == "Buzz":

            buzzTime += 1

            #print(buzz(count, buzzNum))

            buzzLoop.append(buzz(count, buzzNum))

            count += 1

        else:

            #print(buzz(count, buzzNum))

            buzzLoop.append(buzz(count, buzzNum))

            count += 1

    return buzzLoop


print(buzz(11,4))
print(buzz(51, 5))
print(whileBuzz(0, 3))

'''

1. Yes, the simplest solution would be to write a for loop that goes to a very large number and when put condiditons are satisfied, write break() to prevent the loop from running to the set limit

NO, YOU CANT. HAVE TO USE FOR

2. In my case, an empty loop will return. Happens because the conditions of "ending once there has been a number of "Buzz" outputs equal to buzzCount" is satified

3. you could introduce a counter that adds +1 each iteration and when that number is divisible by 2, no output is returned

4. infinitly many times in theory, but on practice, until memmory runs out
'''