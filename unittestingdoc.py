

import unittest


def plus(number1, number2):
    sumMe = number1 + number2
    return sumMe


def minus(number1, number2):
    sumMe = number1 + number2
    return sumMe


def multi(number1, number2):
    sumMe = number1 + number2
    return sumMe


def divide(number1, number2):
    sumMe = number1 + number2
    return sumMe


class MyTest(unittest.TestCase):
    def test(self):
        print("test happened")
        self.assertEquals(plus(2, 2), 4)
        self.assertEquals(minus(2, 2), 0)
        self.assertEquals(multi(2, 2), 4)
        self.assertEquals(divide(2, 2), 1)




