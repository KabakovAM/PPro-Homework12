import csv


class Descriptor:
    def __init__(self):
        self._name = None

    def __get__(self, instance, owner):
        return self._name

    def __set__(self, instance, value: str):
        if value.isalpha() and value[0].isupper():
            self._name = value
        else:
            raise ValueError('Неверный формат ФИО')


class SchoolObjects():
    def __init__(self, name):
        self._name = name
        self._score = []
        self._mark = []

    def __str__(self):
        return (f'{self._name} {self._score} {self._mark}')

    @property
    def score(self):
        return self._score

    @property
    def mark(self):
        return self._mark

    @score.setter
    def score(self, score):
        if 2 <= score <= 5:
            self._score.append(score)
        else:
            raise ValueError('Оценка должна быть неменьше 2 и небольше 5')

    @mark.setter
    def mark(self, mark):
        if 0 <= mark <= 100:
            self._mark.append(mark)
        else:
            raise ValueError('Балл должен быть неменьше 0 и не больше 100')


class Student():
    _first_name = Descriptor()
    _last_name = Descriptor()
    _middle_name = Descriptor()

    def __init__(self, first_name, last_name, middle_name):
        self._first_name = first_name
        self._last_name = last_name
        self._middle_name = middle_name
        self._object_list = []
        with open('Homework12/file.csv', 'r', encoding='utf-8') as data_output:
            csv_read = csv.reader(
                data_output, lineterminator='\n', delimiter=';')
            for line in csv_read:
                ob = SchoolObjects(*line)
                self._object_list.append(ob)

    def print_objects(self):
        for i in range(len(self._object_list)):
            print(self._object_list[i])

    def print_name(self):
        print(f'{self._first_name} {self._last_name} {self._middle_name}')

    def enter_score(self, ob, sc):
        for i in range(len(self._object_list)):
            if self._object_list[i]._name == ob:
                self._object_list[i].score = sc

    def enter_mark(self, ob, mr):
        for i in range(len(self._object_list)):
            if self._object_list[i]._name == ob:
                self._object_list[i].mark = mr

    def average_mark(self, ob):
        result = 0
        for i in range(len(self._object_list)):
            if self._object_list[i]._name == ob:
                for k in range(len(self._object_list[i]._mark)):
                    result += self._object_list[i]._mark[k]
                return round(result / len(self._object_list[i]._mark))

    def average_score(self):
        result = 0
        q = 0
        for i in range(len(self._object_list)):
            for k in range(len(self._object_list[i]._score)):
                result += self._object_list[i]._score[k]
                q += 1
        return round(result / q)


if __name__ == '__main__':
    a = Student('Кабаков', 'Антон', 'Михайлович')
    a.enter_score('Физика', 4)
    a.enter_mark('Математика', 65)
    a.enter_score('Физика', 5)
    a.enter_mark('Математика', 100)
    a.enter_score('Русский язык', 5)
    a.enter_score('Русский язык', 5)
    print(a.average_mark('Математика'))
    print(a.average_score())
    a.print_name()
    a.print_objects()
