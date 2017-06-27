class Numeric:
    def __init__(self, p, q = 1):   # p - целое, q - натуральное
        if q == 0:
            raise Exception('На нуль делить нельзя!')
        if q < 0:   # проверяю, что p - целое, q - натуральное
            p = -p
            q = -q
        if p % 1 == 0:  # чтобы не было 10.0 или как из float перейти в int
            p = int(p)
        if q % 1 == 0:  # чтобы не было 10.0 или как из float перейти в int
            q = int(q)
        # определяем числитель и знаменатель
        self.p = p  # числитель
        self.q = q  # знаменатель

    def evklid(self, a, b):    # алгоритм евклида
        a = abs(a)
        b = abs(b)
        while a != 0:
            if a < b:
                tmp = a
                a = b
                b = tmp
            a = a % b
        return b

    def reduction(self):    # сокращение дроби
        n = self.evklid(self.p, self.q)
        while n != 1:   # пока НОД не стал равен 1, сокращаем
            self.p = self.p // n
            self.q = self.q // n
            n = self.evklid(self.p, self.q)
        return

    def __str__(self):
        if self.q == 1:    # чтобы не было 10/1
            return '{}'.format(self.p)
        if self.p // 1000 >= 1 or self.q // 1000 >= 1:  # округление числа, т.е. если 12483/1243 - то переводится в float
            return '{}'.format((self.p / self.q).__round__(3))   # FIXED! слишком много знаков после запятой
        return '{}/{}'.format(self.p, self.q)   # обычное распечатывание типа 15/28

    def __add__(self, other):   # сложение
        res = Numeric(self.p * other.q + self.q * other.p, self.q * other.q)
        res.reduction()
        return res

    def __sub__(self, other):   # разность
        res = Numeric(self.p * other.q - self.q * other.p, self.q * other.q)
        res.reduction()
        return res

    def __mul__(self, other):   # умножение
        res = Numeric(self.p * other.p, self.q * other.q)
        res.reduction()
        return res

    def inverse(self):  # обратное число
        res = Numeric(self.q, self.p)
        return res

    def __truediv__(self, other):   # деление
        res = self.__mul__(other.inverse())
        return res

    def __pow__(self, other):   # возведение в степень (причем в любую! (вроде))
        res = Numeric(self.p ** (other.p / other.q), self.q ** (other.p / other.q))
        res.reduction()
        return res

    def __lt__(self, other):    # x < y
        if self.p * other.q < other.p * self.q:
            return True
        return False

    def __le__(self, other):    # x ≤ y
        if self.p * other.q <= other.p * self.q:
            return True
        return False

    def __eq__(self, other):    # x == y
        if self.p * other.q == other.p * self.q:
            return True
        return False

    def __ne__(self, other):    # x != y
        if self.p * other.q != other.p * self.q:
            return True
        return False

    def __gt__(self, other):    # x > y
        if self.p * other.q > other.p * self.q:
            return True
        return False

    def __ge__(self, other):    # x ≥ y
        if self.p * other.q >= other.p * self.q:
            return True
        return False

    def __abs__(self):
        return Numeric(abs(self.p), self.q)