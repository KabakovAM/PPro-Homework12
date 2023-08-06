class Square ():
    __slots__ = ('_len_a', '_len_b')

    def __init__(self, len_a=0, len_b=0):
        self._len_a = len_a
        self._len_b = len_b

    def square_length(self):
        print(round(2*self._len_a + 2*self._len_b, 2))

    def square_area(self):
        print(round(self._len_a*self._len_b, 2))

    @property
    def len_a(self):
        return self._len_a

    @property
    def len_b(self):
        return self._len_b

    @len_a.setter
    def len_a(self, len_a):
        if len_a > 0:
            self._len_a = len_a
        else:
            raise ValueError(
                'Длина стороны прямоугольника должна быть больше 0')

    @len_b.setter
    def len_b(self, len_b):
        if len_b > 0:
            self._len_b = len_b
        else:
            raise ValueError(
                'Длина стороны прямоугольника должна быть больше 0')


if __name__ == '__main__':
    a = Square(10, 15)
    print(a.__slots__)
    print(Square.__slots__)
