
def myst(s):
    if len(s) <= 1:
        return True

    elif s[0] != s [len(s) -1]:
        return False

    else:
        return myst (s[1:len(s)-1])

print(myst("noon"))


