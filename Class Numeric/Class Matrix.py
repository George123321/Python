from Class_Numeric import Numeric

class Matrix:
    def __init__(self, n, m):   # n - количество строк, m - количество столбцов
        self.n = n
        self.m = m
        self.list = [[None for i in range(m)] for j in range(n)]

    def write_matrix(self):     # запись в матрицу
        print('Введите строки матрицы, разделяя элементы пробелом')
        for i in range(self.n):
            s = input().split()
            if len(s) != self.m:
                raise Exception('Размер матрицы и количество элементов не совпадают')
            for j in range(self.m):
                s[j] += '|1'
                self.list[i][j] = Numeric(float(s[j].split('|')[0]), float(s[j].split('|')[1]))
        return self

    def print(self):    # печать матрицы
        #if None in self.list[0]:   #FIXME почему-то вылетает, видимо, надо прописать в Numeric проверку наличия в списке
        #    raise Exception('Вы не записали элементы в матрицу!')
        for i in range(self.n):
            print()
            for j in range(self.m):
                print(self.list[i][j], end=' ')
        print()

    def refresh(self):  # обновляет размеры матрицы
        self.n = len(self.list)
        self.m = len(self.list[0])

    def trans(self):    # транспонирование матрицы
        #if None in self.list[0]:   #FIXME почему-то вылетает, видимо, надо прописать в Numeric проверку наличия в списке
        #    raise Exception('Вы не записали элементы в матрицу!')
        B = Matrix(self.m, self.n)
        for i in range(self.n):
            for j in range(self.m):
                B.list[j][i] = self.list[i][j]
        self.list[:] = B.list
        self.refresh()
        return self


    def skal_proizv(self, a, b):
        if len(a) != len(b):
            raise Exception('Векторы имеют разную длину')
        res = Numeric(0)
        for i in range(len(a)):
            res += a[i] * b[i]
        # print('Скалярное произведение векторов =', res)
        return res

    def __add__(self, other):   # сумма матриц
        #if None in self.list[0] or None in other.list[0]:   #FIXME почему-то вылетает, видимо, надо прописать в Numeric проверку наличия в списке
        #    raise Exception('Вы не записали элементы в одну из матриц!')
        if self.n != other.n or self.m != other.m:
            raise Exception('Матрицы разных размеров!')
        print('Результат суммы матриц:', end='')
        res = Matrix(self.n, self.m)
        for i in range(self.n):
            for j in range(self.m):
                res.list[i][j] = self.list[i][j] + other.list[i][j]
        return res

    def __sub__(self, other):  # разность
        #if None in self.list[0] or None in other.list[0]:   #FIXME почему-то вылетает, видимо, надо прописать в Numeric проверку наличия в списке
        #    raise Exception('Вы не записали элементы в одну из матриц!')
        if self.n != other.n or self.m != other.m:
            raise Exception('Матрицы разных размеров!')
        print('Результат разности матриц:', end='')
        res = Matrix(self.n, self.m)
        for i in range(self.n):
            for j in range(self.m):
                res.list[i][j] = self.list[i][j] - other.list[i][j]
        return res

    def __mul__(self, other):  # умножение
        pass    # FIXME чет не робит пока
        '''
        res = Matrix(self.n, other.m)
        other.trans()
        for i in range(self.n):
            for j in range(other.n):
                res.list[i][j] = self.skal_proizv(self.list[i], other.list[j])
        res.refresh()
        return res
        '''


A = Matrix(2, 2)
A.write_matrix()
B = Matrix(2, 2)
B.write_matrix()
(A-B).print()

