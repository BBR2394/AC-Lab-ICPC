def multiply(a, b, x, y):
    return x * (a + b) + a * y, a * x + b * y


def square(a, b):
    a2 = a * a
    b2 = b * b
    ab = a * b
    return a2 + (ab << 1), a2 + b2


def power(a, b, m):
    if m == 0:
        return (0, 1)
    elif m == 1:
        return (a, b)
    else:
        x, y = a, b
        n = 2
        while n <= m:
            # repeated square until n = 2^q > m
            x, y = square(x, y)
            n = n * 2
        # add on the remainder
        a, b = power(a, b, m - n // 2)
        return multiply(x, y, a, b)


def implicit_fib(n):
    a, b = power(1, 0, n)
    return a


def suiteAntoine(param):
    pass


def fib(n, schema):
    tab = ['0', '1']

    position = 0
    while schema not in tab[1]:
        suivant = tab[1] + tab[0]
        tab[0] = tab[1]
        tab[1] = suivant
        position += 1

    #suivant = tab[1] + tab[0]

    if position % 2 == 1:
        f = implicit_fib(n - position)
    else:
        if schema == suivant:
            f = implicit_fib(n - position + len(suivant.split(schema)))/2
        else:
            f = implicit_fib(n - position + len(suivant.split(schema))) - 1
    return f


if __name__ == '__main__':
    n = 6
    schema = '01'
    print(fib(n, schema))
