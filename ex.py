def high_and_low(numbers):

    lst = list()
    for n in numbers:
        if n == ' ': continue
        print(n)
        i = int(n)
        lst.append(i)
        m = max(lst)
        mi = min(lst)

    return f'"{m} {mi}"'



high_and_low('1 9 3 4 -5')
a = '-4'
b = int(a)
#print(dir(type(a)))
