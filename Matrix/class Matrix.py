class Matrix:
    def __init__(self, n, m): # n - количество строк, m - количество столбцов
        self.n = n
        self.m = m
        self.list = []
    def write_matrix(self):
        print('Введите строки матрицы, разделяя элементы пробелом')
        for i in range(self.n):
            self.list.append([int(x) for x in input().split()])
        return self.list
    def matrix_2D(self):  # Печатает матрицу
        for i in range(self.n):
            print(*self.list[i])
        print()
    def skal_proizv(self, b):
        if len(self.list) != len(b):
            raise Exception('Векторы имеют разную длину')
        res = 0
        for i in range(len(self.list)):
            res += self.list[i] * b[i]
        # print('Скалярное произведение векторов =', res)
        return res
    def trans_matrix(self):
        B = [[] for i in range(len(self.list[0]))]
        for i in range(len(self.list)):
            for j in range(len(self.list[0])):
                B[j].append(self.list[i][j])
        self.n = self.m
        self.m = self.n
        self.list = B
    def matrix_multiply(self, B):
        C = [[] for i in range(len(self.list))]
        B = B.trans_matrix
        for i in range(len(self.list)):
            for j in range(len(B)):
                C[i].append(self.list[i].skal_proizv(B[j]))
        res = Matrix(self.n, len(B[0]))
        res.list = B
        return res

a = Matrix(3, 4)
a.write_matrix()
sfsdf = Matrix(4, 3)
sfsdf.write_matrix()
a.matrix_2D()
sfsdf.matrix_2D()
C = a.matrix_multiply(sfsdf)

