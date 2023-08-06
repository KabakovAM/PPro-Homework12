class Factorial():
    _res_list = []

    def __init__(self, q):
        self.q = q

    def __call__(self, num):
        res = 1
        for i in range(1, num+1):
            res = res * i
        if len(self._res_list) < self.q:
            self._res_list.append((num, res))
        else:
            self._res_list.pop(0)
            self._res_list.append((num, res))
        return res
    
    def show_res(self):
        for i in range(len(self._res_list)):
            print(self._res_list[i])


if __name__ == '__main__':
    a = Factorial(3)
    print(a(5))
    print(a(4))
    print(a(3))
    print(a(2))
    print(a(6))
    print(a(7))
    print(a(10))
    a.show_res()