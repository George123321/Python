class Matrix:
    def __init__(self):
        A = [[]]
        n = len(A)
        m = len(A[0])
        self.A = A
        self.n = n
        self.m = m

    def write_matrix(self):
        print('Введите количество строк матрицы')
        print('Введите строки матрицы, разделяя элементы пробелом')
        for i in range(self.n):
            self.A.append([int(x) for x in input().split()])
        return self.A

    def matrix_2D(self):  # Печатает матрицу
        for i in range(self.n):
            print(*self.A[i])
        print()

a = Matrix()
a.write_matrix()
a.matrix_2D()

