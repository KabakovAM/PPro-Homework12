import json


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

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open('res.json', 'a') as data_input:
            json.dump(self._res_list, data_input, indent=4)

    def show_res(self):
        for i in range(len(self._res_list)):
            print(self._res_list[i])


if __name__ == '__main__':
    a = Factorial(3)
    with a as b:
        print(b(5))
        print(b(4))
        print(b(3))
