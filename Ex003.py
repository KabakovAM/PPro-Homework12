class Factorial():

    def __init__(self, stop, start=1, step=1):
        self.stop = stop
        self.start = start
        self.step = step
        self.res = 1
        self.first = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.first == 1:
            self.res = self.res * self.start
            self.start += 1
            self.first += 1
            return self.res
        elif self.first + self.step <= self.stop + 1:
            for _ in range(self.step):
                self.res = self.res * self.start
                self.start += 1
                self.first += 1
            return self.res
        raise StopIteration


if __name__ == '__main__':
    a = Factorial(stop=7, start=1, step=3)
    for i in a:
        print(i)
