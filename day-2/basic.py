def func(x) :
    res = 0

    for i in range(x):
        res += i
        print(res)
    return res

print(func(4))