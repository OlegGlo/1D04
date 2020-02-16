'''

List operations:
.append
.pop
.remove
.insert
.index
etc

find:
print(<value>, end = ' ') the end part specifially

ACII characters in a string

print(string[0:3])


string opperations:
+
*
len()
index through string

etc

ord()

chr()

SEQUENCES -  is an enumerated collection of objects inwhich repetitions are allowed.

the built in sequences include: 

    str (immutable ASCII strings)

    list (mutable list of values)
'''

samplelist = [1,2,3,4,5]
samplelist2 = [6,7]
samplestring = "example"
samplestring2 = " yeet"

def listexamples(list1,string1,list2,string2):
    #Lists start counting from 0 (1st number in a list is a position 0)
    print(
        list1, #shows the contents in the variables
        string1 
    )

    print(
        len(list1), #shows the length of the list
        len(string1)
    )

    print(
        len(list1), #shows the length of the list
        len(string1)
    )

    print(
        list1+list2, #combines string with string and list with list
        string1+string2
    )

    print(
        list1[0], #prints the 2nd value in the sequence, remeber that sequences start at 0.
        string1[0]
    )

    print(
        list1[1]*2, #here, the second valus is multipled by 2 and printed
        string1[1]*2 #here, the second letter is printed twice
    )

    print(
        list1[2:4], #here, only the 3 through 5 value is printed
        string1[2:4]
    )

    print(
        list1[2:], #here, the variables are printed from the 3 number onwards
        string1[2:]
    )

#listexamples(samplelist,samplestring,samplelist2,samplestring2) # showcases operators shared by both sequence types

'''
LISTS
- finite array of values
- in python, arrays can contain different data types
- lists are mutable - Values can be changed

STRINGS
- finite sequence of characters
- are defined with single or double quote marks
- lists are immutable - Values cannot be changed

- non printable characters (e.g newline) are represented with a backslash (\n)
'''


'''
Python OBJECTS + METHODS

all data types in python are objects with predefined methods, for lists and strings we have:

'''

def anotherlistexample(samplelist,samplestring):

    #LISTS

    samplelist.append(6) #adds the value '6' to the end of the list 

    samplelist.pop() #removes and returns the last value in the list, in this case '6'

    samplelist.remove(2) #removes a value in the list, in this case looks for '2' and removes it

    samplelist.insert(2,8) #insert a value before the index, in this case goes to position '4' and adds '1'. All other values are moved down 1 position.

    value = samplelist.index(3) #returns an items location in the list

    #STRINGS

    value = samplestring.startswith("m") #returns true or false if conditions are matched

    value = samplestring.endswith("e") #returns true or false if conditions are not matched

    value = samplestring.rfind("p") #finds the rightmost p and returns its position value

    

    print('end')

anotherlistexample(samplelist,samplestring)









'''

00100100


'''