
def base():

    b = "hello, Jupyter"
    c = ""

    for a in b:
        c += chr(ord(a)-10)

    print(c)



def option4():

    b = "hello, Jupyter"
    c = ""

    for i in range(len(b)):

        c += chr(ord(b[i])-10)

    print(c)

base()
option4()