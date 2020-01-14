#Lecture 1 examples

def PlusEqualsOperator():
    '''
    1.1

    # Plus-Equal Operator

    counter = 0
    counter += 10

    # This is equivalent to

    counter = 0
    counter = counter + 10

    # The operator will also perform string concatenation

    message = "Part 1 of message "
    message += "Part 2 of message"

    E.g:

    '''

    Message1 = "part 1 "
    Message1 += "part 2"

    print(Message1) #this will print "part1 part2"

def PythonString():
    first = "Hello "
    second = "World"

    result = first + second

    long_result = first + second + "!"

    print(long_result) #this will print "Hello World!"

def DataTypes():
    #Use function type() to test which the datatype a variable is

    #--------

    boolDataType = True #bool data type

    #Note: has to start with capital T otherwise does not work

    print(type(boolDataType)) #this will output the data types name
    print("---")

    #--------

    RandomNumber = 12.34 #A random variable

    print(type(int(RandomNumber))) 
    print(int(RandomNumber))
    print("Above: type 'int' Experssion: 12 \n" + "---")
    

    print(type(float(RandomNumber))) 
    print(float(RandomNumber))
    print("Above: type 'float' Experssion: 12.34 \n" + "---")

    print(type(RandomNumber))
    print(RandomNumber)
    print("Above: type 'float but it is automatically defined as that by Python' Experssion: 12.34 \n" + "---")

    RandomString = "D04 is chill" #A random string

    print(type(RandomString))
    print(RandomString)
    print("Above: type 'string' Experssion: 'D04 is chill' \n" + "---")

    RandomList = ["value",69,420] #A random sent of variables and data types

    print(type(RandomList))
    print(RandomList[0] + str(RandomList[1]) + str(RandomList[2]))
    print("Above: type 'list' Experssion: 'value69420' which all the values in the list combined \n" + "---")

def Constants():

    CONSTANT = 12.34 #constant

    addition = 0 #variable

    addition = 1 + CONSTANT 

    print(addition)

def Statements():

    #most of these his will be covered later on for now remeber:

    #FOR LOOPS
    #are used for definite loops

    aList = ["this","is","an","example"]
    for number in aList:
        print (number)

    #this runs through 'aList' and prints the strings contained within it
    #'number' is a variable that holds the temporary information contained in the current iteration of the loop

    print("-----")

    #WHILE LOOPS
    #are used for indefinite loops

    i = 1
    while i < 6:
        print(i)

        i += 1

    #this loop will continously add 1 to i until i reaches 6, after which the contition given (i < 6)
    #ceases to be true, ending the loop



PlusEqualsOperator()
PythonString()
DataTypes()
Constants()
#Statements()

#use comments to turn on or off each example

#COMMENTS

#use the hashtag for one line comments

'''

use these

if you want to write a long explanation

'''


#fuck myself

