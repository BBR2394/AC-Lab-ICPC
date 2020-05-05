import pytest


def fib_pair(n):
    tab = [1, 1]
    for c in range(n - 1):
        suivant = tab[1] + tab[0]
        tab[0] = tab[1]
        tab[1] = suivant
    return tab[1]


def fib_inpair(n):
    tab = [1, 3]
    for c in range(n - 2):
        suivant = tab[1] + tab[0]
        tab[0] = tab[1]
        tab[1] = suivant
    return tab[1]


def fib_autre(n):
    tab = [1, 1]
    compt = 0
    for c in range(n):
        compt += 1
        suivant = tab[1] + tab[0]
        tab[0] = tab[1]
        tab[1] = suivant
        if compt % 2 == 1:
            tab[1] += 1
    return tab[1] - 1


def fib_sepeciale(n):
    tab = [1, 3]
    compt = 0
    for c in range(n - 2):
        compt += 1
        suivant = tab[1] + tab[0]
        tab[0] = tab[1]
        tab[1] = suivant
        if compt % 2 == 0:
            tab[1] += 1
    return tab[1]


def fib(n, schema):
    tab = ['0', '1']

    position = 1
    while schema not in tab[1]:
        suivant = tab[1] + tab[0]
        tab[0] = tab[1]
        tab[1] = suivant
        position += 1

    suivant = tab[1] + tab[0]

    if tab[1] != schema:
        if len(suivant) % 2 != 0:
            return fib_inpair(n - position)
        else:
            return fib_autre(n - position)
    else:
        if len(tab[1]) % 2 != 0:
            return fib_sepeciale(n - position)
        else:
            return fib_pair(n - position)


class TestClass:
    def test_1(self):
        assert 5 == fib(6, '10')

    def test_2(self):
        assert 8 == fib(7, '10')

    def test_3(self):
        assert 4 == fib(6, '01')

    def test_4(self):
        assert 4 == fib(6, '101')

    def test_5(self):
        assert 7540113804746346428 == fib(96, '10110101101101')


if __name__ == '__main__':
    TestClass()
