
def exam1(x):
    try:
        a=x
        b=x[:]

        return a/b

    except ZeroDivisionError:
        return 1
    except IndexError:
        return 2
    except TypeError:
        return 3

L = []
print(exam1(L))



