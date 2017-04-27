def skal_proizv(a, b):
    if len(a) != len(b):
        raise Exception('Векторы имеют разную длину')
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
    print('Введите строки матрицы, разделяя элементы пробелом')
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

def podmatrix_for_first_stroke(A, j):
    B = []
    A = A[1:] + A[0:1]
    for i in range(len(A)-1):
        B.append(A[i][0:j] + A[i][j+1:])
    return B

def det(A):
    res = 0
    z = 0
    if len(A) != len(A[0]):
        raise Exception("Матрица не является квадратной")
    if len(A[0]) == 1: #Крайний случай
        return int(A[0][0])
    else:
        for j in range(len(A[0])):
            z = det(podmatrix_for_first_stroke(A, j))
            res += (-1)**(j)*A[0][j]*z
    return res

def podmatrix(A, i, j):
    B = []
    A = A[:i] + A[i+1:]
    for k in range(len(A)):
        B.append(A[k][0:j] + A[k][j + 1:])
    return B


def invert_matrix(A):
    d = det(A)
    if d == 0:
        raise Exception("Матрица вырождена")
    if len(A) != len(A[0]):
        raise Exception("Матрица не является квадратной")
    B = [[0*len(A)]*len(A) for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A)):
            B[i][j] = (-1)**(i+j)*(det(podmatrix(A, i, j))/d)
    return trans_matrix(B)

A = write_matrix()
matrix_2D(invert_matrix(A))