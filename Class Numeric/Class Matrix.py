from Class_Numeric import Numeric

class Matrix:
    def __init__(self, n, m):   # n - количество строк, m - количество столбцов
        self.n = n
        self.m = m
        self.list = [[None for i in range(m)] for j in range(n)]

    def write_matrix(self):
        print('Введите строки матрицы, разделяя элементы пробелом')
        for i in range(self.n):
            s = input().split()
            for j in range(self.m):
                s[j] = s[j] + '|1'
                self.list[i][j] = Numeric(float(s[j].split('|')[0]), float(s[j].split('|')[1]))
        return self.list

A = Matrix(3, 3)
A.write_matrix()
print(A.list)