def myfun(**kwargs):
    for key,value in kwargs.items():
        print("%s == %s" % (key, value))

myfun(first="thunder", mid="soft", last="india")
