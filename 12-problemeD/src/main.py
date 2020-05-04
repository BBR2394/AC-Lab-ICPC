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
        if compt % 2 == 1 :
            tab[1] += 1
    return tab[1]

def fib_sepeciale(n):
    tab = [1, 3]
    compt = 0
    for c in range(n - 2):
        compt += 1
        suivant = tab[1] + tab[0]
        tab[0] = tab[1]
        tab[1] = suivant
        if compt % 2 == 0 :
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

    if tab[1] != schema :
        if len(suivant)%2 != 0:
            return fib_inpair(n - position)
        else:
            return fib_autre(n - position)
    else :
        if len(tab[1]) % 2 != 0:
            return fib_sepeciale(n - position)
        else:
            return fib_pair(n - position)

    # if len(schema) % 2 == 0:
    #     if len(tab[1]) % 2 == 0:
    #         if tab[1] != schema :
    #             return fib_autre(n - position)
    #         else :
    #             return fib_pair(n - position)
    #     else :
    #         return fib_inpair(n - position)
    # else:
    #     return fib_sepeciale(n - position)


if __name__ == '__main__':
    n = 7
    schema = '10'
    print(fib(n, schema))
