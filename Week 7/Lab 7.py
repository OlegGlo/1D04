
'''
Lab 7 - minor

Review:

.split() - converts from string to list

.join() - converts from list to string

'''

#join demo
def demo():
    strlist = ['H', 'e', 'l', 'l', 'o']
    print("*".join(strlist))

#demo()




#function demo
def demo2():
    double = x * 2
    quad = x * 4
    return double, quad

#answ = demo2(2)
#print(answ[1]) # using the touple method



#exception handling

def demo3(x):

    try:
        foo = 1/(x**2)

        return foo

    except:

        return "error"

#print(demo3(0))



#ACTUAL LAB

def breakSentence(string):

    foo = string.split()

    return foo

def combineSentence(strList):

    foo = " ".join(strList)

    return foo

def breakParagraph(paragraph):

    foo2 = []

    foo1 = paragraph.split("\n")

    for i in range(len(foo1)):
        foo2.append(foo1[i].split())

    return foo2

def combineParagraph(parList):

    try:

        foo1 = []

        for i in range(len(parList)):
            foo1.append(" ".join(parList[i]))

        foo2 = "\n".join(foo1)

        return foo2

    except:

        return "broken"

print(breakSentence("I will be there for you"))
print(combineSentence(['I', 'will', 'be', 'there', 'for', 'you']))
print(breakParagraph("I will be there for you\nwhen the rain starts to pour"))

#print(combineParagraph([["I","will","be","there",'for','you'],['when', 'the', 'rain', 'starts', 'to', 'pour']]))
print(combineParagraph(1))

'''
LAST TWO SECTIONS

error:
instead of a list put in a number and run it, there will be an error so we can a try/except statement

long ans:

test cases:

'''