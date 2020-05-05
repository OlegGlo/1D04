def func(x):
    print(x)
    if type(x) != int:

        raise(NameError)

    print("done")

func(10)

