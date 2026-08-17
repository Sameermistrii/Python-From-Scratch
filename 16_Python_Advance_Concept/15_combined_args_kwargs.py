def func1(*args, **kwargs):
    print(args)
    print(kwargs)

func1(1, 2, 4, 5, jack=34, jill=32, marie=31)