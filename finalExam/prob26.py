
iniString = "ENG 1D04"

def op1(iniString):

    c = iniString.index(" ")
    finString = iniString[c+2:]
    print(finString)

op1(iniString)

def op2(iniString):

    c = iniString.index("4")
    finString = iniString[c-2:]
    print(finString)

op2(iniString)
