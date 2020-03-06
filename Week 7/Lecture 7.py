

'''
while loops

different things you could do with them

exceptions to the rules, copy down for tests




'''

def main():
    total = 0.0
    moredata = "Yes"

    while moredata[0] == "Yes":
        x = float(input("enter num: "))
        total = total + x
        moredata = input("enter more?: ")

    print("the total is", total)

main()

a = 1
b=2
c=3


def main2():
    while a <= b <= c:
        print(b)

        break

main2()

def main3():

    while a <= b:
        while b <= c:
            print(c)

            break

def main3():
    a = 2
    b = 5
    c = 4

    while(a or b and not c):
        print("fuck")
        a = a -1 

#order: not, and, or

main3()


