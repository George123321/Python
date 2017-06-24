def evklid(a, b):
    while a != 0:
        if a < b:
            tmp = a
            a = b
            b = tmp
        a = a % b
    return b

print(evklid(100, 25))