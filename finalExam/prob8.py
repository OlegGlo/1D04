
def getAge(age):
    phrase = ''
    if(age < 16):
        phrase = phrase + "cant drink,drive,vote"
    if(age >= 16):
        phrase = phrase + "can drive but no rest"
    if (age >= 18):
        phrase = phrase + "cant ddrink"
    if (age >= 19):
        phrase = phrase + "can all"

    return phrase

def main():
    a = input("enter age")
    print(getAge(int(a)))

main()

