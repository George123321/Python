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
            raise Exception('Попытка перемножить строку и столбец разной длины')
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
        if d == Numeric(0):
            raise Exception("Матрица вырождена")
        #if self.n != self.m:   # Уже проверяется при подсчете детерминанта
        #    raise Exception("Матрица не является квадратной")
        B = Matrix(self.n, self.n)
        for i in range(self.n):
            for j in range(self.n):
                B.list[i][j] = (Numeric(-1)) ** (Numeric(i + j)) * (self.podmatrix(i, j).det() / d)
        return B.trans()

    #def Gauss(self):
    #    for i in range(self.m): # сначала смещаем все строки, где первый элемент нуль, вниз
    #        if
    #        for k in range(i, self.n):

    def gauss(self):
        for i in range(self.n):
            k = i
            if k + 1 > self.m:  # если это случилось, то алгоритм вылетет
                break
            '''
            дальше хитрожопый подгон на проверку того, что элемент нулевой (частный случай), и делает перестановку
            '''
            while k < self.n and self.list[k][i] == Numeric(0):     # проверят, не нулевой ли первый элемент
                k += 1
            '''
            по выходе имеем либо весь столбец нули, либо нашли ненулевой элемент
            '''
            if k == self.n and self.list[k - 1][i] == Numeric(0):
                continue
            else:
                if k != i:
                    self.list[k][i], self.list[i][i] = self.list[i][i], self.list[k][i]
                    print('Поменяем местами', k + 1, '- ю и', i + 1, '- ю строки')
            '''
            в данный момент мы сделали так, что первый элемент не нуль. Делим!
            '''
            for k in range(i + 1, self.n):
                if self.list[k][i] != Numeric(0):
                    q = self.list[k][i] / self.list[i][i]
                    print('Из', k + 1, '- ой строки вычтем', q, i + 1, '- ых строк')
                    for j in range(i, self.m):
                        #q = tmp / self.list[i][i]
                        self.list[k][j] -= q * self.list[i][j]
        '''
        в этот момент есть 2 варианта: последняя (последние) строки нулевые, либо там есть элементы. В первом варианте
        нужно пропустить нулевые строки и перейти к тем, где есть элементы, а во втором мы уже там
        '''
        p = '123'   # если p осталось '123', значит последние строки не нулевые
        for i in range(self.n):
            if self.list[i] == [Numeric(0) for k in range(self.m)]:
                p = i - 1   # p - номер строки, где есть элементы
                break
        if p == '123':
            p = self.n - 1
        '''
        разделим последнюю строчку так, чтобы на диагонали появлялись единицы. Номер этой строки - p
        '''
        for j in range(self.m):
            if self.list[p][j] != Numeric(0):
                tmp = self.list[p][j]
                l = j
                break
        if p >= 0 and tmp != Numeric(1):  # это условие значит, что матрица не нулевая
            for j in range(l, self.m):
                self.list[p][j] /= tmp
            print('Разделим', p + 1, '- ю строку на', tmp)
        if p < 0:   # это условие значит, что матрица нулевая
            return self
        '''
        на этом моменте прямой ход алгоритма гаусса закончен. p указывает на ненулевую строку
        '''
        return self

    def gauss_trans(self):  # функция транспонирует матрицу по побочной диагонали, а потом как обычно
        res = Matrix(self.n, self.m)
        for i in range(self.n):
            for j in range(self.m):
                res.list[i][j] = self.list[self.n-1-i][self.m-1-j]
        return res










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
    def __init__(self, n, m = 1.1):
        super(Zero_Matrix, self).__init__(n, m)
        self.contain()

    def contain(self):
        self.list[:] = [[Numeric(0) for i in range(self.m)] for j in range(self.n)]
        return self