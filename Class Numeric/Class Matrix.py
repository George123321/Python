from Class_Numeric import Numeric

class Matrix:
    def __init__(self, n, m = 1.1):   # n - количество строк, m - количество столбцов
        if m == 1.1:
            m = n
        self.n = n
        self.m = m
        self.list = [[None for i in range(m)] for j in range(n)]

    def write_matrix(self):     # запись в матрицу
        print('Введите строки матрицы, разделяя элементы пробелом (дробные числа, например 1/2, вводить в виде 1|2)')
        for i in range(self.n):
            s = input().split()
            if len(s) != self.m:
                raise Exception('Размер матрицы и количество элементов не совпадают')
            for j in range(self.m):
                s[j] += '|1'
                self.list[i][j] = Numeric(float(s[j].split('|')[0]), float(s[j].split('|')[1]))
        return self

    def print(self):    # печать матрицы
        if None in self.list[0]:
            raise Exception('Вы не записали элементы в матрицу!')
        for i in range(self.n):
            print()
            for j in range(self.m):
                print(self.list[i][j], end=' ')
        print()

    def refresh(self):  # обновляет размеры матрицы
        self.n = len(self.list)
        self.m = len(self.list[0])

    def trans(self):    # транспонирование матрицы
        if None in self.list[0]:
            raise Exception('Вы не записали элементы в матрицу!')
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
        if None in self.list[0] or None in other.list[0]:
            raise Exception('Вы не записали элементы в одну из матриц!')
        if self.n != other.n or self.m != other.m:
            raise Exception('Матрицы разных размеров!')
        print('Результат суммы матриц:', end='')
        res = Matrix(self.n, self.m)
        for i in range(self.n):
            for j in range(self.m):
                res.list[i][j] = self.list[i][j] + other.list[i][j]
        return res

    def __sub__(self, other):  # разность
        if None in self.list[0] or None in other.list[0]:
            raise Exception('Вы не записали элементы в одну из матриц!')
        if self.n != other.n or self.m != other.m:
            raise Exception('Матрицы разных размеров!')
        print('Результат разности матриц:', end='')
        res = Matrix(self.n, self.m)
        for i in range(self.n):
            for j in range(self.m):
                res.list[i][j] = self.list[i][j] - other.list[i][j]
        return res

    def __mul__(self, other):  # умножение
        if None in self.list[0] or None in other.list[0]:
            raise Exception('Вы не записали элементы в одну из матриц!')
        res = Matrix(self.n, other.m)
        other.trans()
        for i in range(self.n):
            for j in range(other.n):
                res.list[i][j] = self.skal_proizv(self.list[i], other.list[j])
        res.refresh()
        return res

    def podmatrix(self, l, s):  # создает подматрицу, выбивая l-ую строку и s-ый столбец
        B = Matrix(self.n, self.m)
        B.list[:] = self.list[:l] + self.list[l+1:]
        B.refresh()
        B.trans()
        B.list[:] = B.list[:s] + B.list[s+1:]
        B.refresh()
        B.trans()
        B.refresh()
        return B

    def det(self):
        res = Numeric(0)
        z = Numeric(0)
        if self.n != self.m:
            raise Exception("Матрица не является квадратной")
        if len(self.list[0]) == 1:  # Крайний случай
            return self.list[0][0]
        else:
            for j in range(len(self.list[0])):
                m = self.podmatrix(0, j)
                z = m.det()
                res += (Numeric(-1)) ** (Numeric(j)) * self.list[0][j] * z
        return res

    def invert_matrix(self):
        d = self.det()
        if d == 0:
            raise Exception("Матрица вырождена")
        #if self.n != self.m:   # Уже проверяется при подсчете детерминанта
        #    raise Exception("Матрица не является квадратной")
        B = Matrix(self.n, self.n)
        for i in range(self.n):
            for j in range(self.n):
                B.list[i][j] = (Numeric(-1)) ** (Numeric(i + j)) * (self.podmatrix(i, j).det() / d)
        return B.trans()

class Identity_Matrix(Matrix):
    def __init__(self, n):
        super(Identity_Matrix, self).__init__(n, n)
        self.contain()

    def contain(self):
        if self.n != self.m:
            raise Exception('Единичная матрица должна быть квадратной')
        self.list[:] = [[Numeric(0) for i in range(self.m)] for j in range(self.n)]
        for i in range(self.n):
            self.list[i][i] = Numeric(1)
        return self

class Zero_Matrix(Matrix):
    def __init__(self, n, m):
        super(Zero_Matrix, self).__init__(n, m)
        self.contain()

    def contain(self):
        self.list[:] = [[Numeric(0) for i in range(self.m)] for j in range(self.n)]
        return self