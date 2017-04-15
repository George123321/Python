def skal_proizv(a, b):
    if len(a) != len(b):
        print('Векторы имеют разную длину')
        return
    res = 0
    for i in range(len(a)):
        res += a[i]*b[i]
    #print('Скалярное произведение векторов =', res)
    return res

def write_vec():
    print('Введите координаты вектора в строку через пробел')
    return list(map(int, input().split()))


def write_matrix():
    A = []
    print('Введите количество строк матрицы')
    n = int(input())
    for i in range(n):
        A.append([int(x) for x in input().split()])
    return A

def matrix_2D(A): #Печатает матрицу
    for i in range(len(A)):
        print(*A[i])
    print()

def trans_matrix(A):
    B = [[] for i in range(len(A[0]))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            B[j].append(A[i][j])
    return B

def matrix_multiply(A, B):
    C = [[] for i in range(len(A))]
    B = trans_matrix(B)
    for i in range(len(A)):
        for j in range(len(B)):
            C[i].append(skal_proizv(A[i], B[j]))
    return C