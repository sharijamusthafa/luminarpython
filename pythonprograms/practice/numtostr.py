def numtostr(arg):
    switcher={
        0:"zero",
        1:"one",
        2:"two",
    }
    return switcher.get(arg,"nothing")
print(numtostr(0))