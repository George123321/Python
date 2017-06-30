from Class_Numeric import Numeric

def evklid(a, b):
    while a != 0:
        if a < b:
            tmp = a
            a = b
            b = tmp
        a = a % b
    return b

def trans_matrix(A):
    B = [[] for i in range(len(A[0]))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            B[j].append(A[i][j])
    return B

def poadmatrix(A, l, s):
    B = []
    B[:] = A[:l] + A[l+1:]
    B[:] = trans_matrix(B)
    B[:] = B[:s] + B[s+1:]
    B[:] = trans_matrix(B)
    return B



A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = poadmatrix(A,1,0)
print(B)
