from Class_Numeric import Numeric

def evklid(a, b):
    while a != 0:
        if a < b:
            tmp = a
            a = b
            b = tmp
        a = a % b
    return b

a = [[Numeric(1, 2), Numeric(0), None]]
if None in a[0]:
    print('Y')