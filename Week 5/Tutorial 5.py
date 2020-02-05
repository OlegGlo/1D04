
'''
random methods:

random.random() - 0 to 1

random.randint(a,b) - a rand between a and b

random.randrange(start, stop, step) - similar to range function

random.choice() random from a non - sequence - ??????????

File handling:

closing and opening a notebook

Graphics: 

pip install graphics.py

practice - importing grades from a file and shoving it in a array of gpas
and create a bar chart with "pylab" - > import pylab

LEARN PYLAB

look what strip(",")

'''

#from graphics import *

def main():
    win = GraphWin("My Circle", 1000, 1000)
    c = Circle(Point(50,50), 10)
    c.draw(win)
    win.getMouse() # pause for click in window
    win.close()

#main()

def example():

    win = GraphWin()
    win.setCoords(0.0,0.0,10.0,10.0)
    c1 = Circle(Point(3,5),3)
    c1.setFill('red')
    c2=c1 #.clone()           # this will point to the same varibale, can use method .clone() to duplicate it!!
    c2.setFill('blue')
    c2.move(4,0)
    c1.draw(win)
    c2.draw(win)

    win.getMouse()
    win.close()

#example()

def practice2Major():

    file = open('lab6example.txt','r')
    content = file.read()
    file.seek(0,0)
    content2 = file.readlines()

    L = []
    Intermed = []

    sumAB = 0
    sumB = 0

    firstnum = []
    secondnum = []

    L = []
    anEntry = []

    #exampleee = content2[0].strip().split(",")

    for index in range(len(content2)):  # putting numbers into lists
        splitted = content2[index].strip().split(",")

        firstnum.append(float(splitted[0]))
        secondnum.append(float(splitted[1]))

        anEntry = [firstnum[index],secondnum[index]]

        L.append(anEntry)

        print(L[index])


    for index in range(len(content2)):
        sumAB += firstnum[index] * secondnum[index]
        sumB += secondnum[index]

    V = sumAB/sumB
    print(V)

    file.close()
    
practice2Major()

# a list of these

# V =  





