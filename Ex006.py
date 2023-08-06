class Descriptor:
    def __init__(self):
        self._len = 0

    def __get__(self, instance, owner):    
        return self._len

    def __set__(self, instance, value):
        if value > 0:
            self._len = value
        else:
            raise ValueError('Длина стороны прямоугольника должна быть больше 0')

class Square():
    _len_a = Descriptor()
    _len_b = Descriptor()

    def __init__(self, len_a, len_b):
        self._len_a = len_a
        self._len_b = len_b

    def square_length(self):
        print(round(2*self._len_a + 2*self._len_b, 2))

    def square_area(self):
        print(round(self._len_a*self._len_b, 2))


if __name__ == '__main__':
    a = Square(10, 4)
    a.square_area()
