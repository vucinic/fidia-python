def say_n_hello(n):
    """
    Queta funzione serve a stampare n volte 'Hello'
    :param n: Questo e` il param che decide il numero di volte
    :return:
    """
    for i in range(n):
        print('Hello')
    n = 0
    print(f'N interno {n}')
    return


def rect_area_per(a, b):
    return a * b, rect_per(a, b)


def rect_per(*sides):
    if len(sides) >= 3:
        return 'Hai sbagliato'

    if len(sides) == 1:
        return sides[0] * 4

    return sides[0] * 2 + sides[1] * 2


def vol_parallelepipedo(b, a, p):
    return a * b * p


def print_words(*words, maiuscolo):
    for e in words:
        # print(e.upper() if maiuscolo else e)
        if maiuscolo:
            print(e.upper())
        else:
            print(e)


def print_kwords(maiuscolo, **kwords):
    # maiuscolo = bool(kwords.get('maiuscolo', False))

    for k, v in kwords.items():
        # print(e.upper() if maiuscolo else e)
        if maiuscolo:
            print(k, v.upper())
        else:
            print(k, v)


def print_words_l(words, maiuscolo):
    for e in words:
        # print(e.upper() if maiuscolo else e)
        if maiuscolo:
            print(e.upper())
        else:
            print(e)


def cube_volume(side_length):
    return 0 if side_length < 0 else side_length ** 3


def main():
    n = 10
    L = ['Ciao', 'pippo', 'pluto']
    # print_words_l(L, maiuscolo=True)
    print_words(*L, maiuscolo=True)
    # print_words(L[0], L[1], L[2], L[3], L[4], maiuscolo=True)
    print(*L)

    d = dict(
        a='123',
        b='CAsd',
        casa=123,
        fdisi4=12.45,
        maiuscolo='False'
    )

    print_kwords(False,
                 a='123',
                 b='CAsd',
                 casa=123,
                 fdisi4=12.45,
                 maiuscolo='False')
    print_kwords(**d)

    res = rect_area_per(3, 4)
    area = res[0]
    per = res[1]

    area, per = rect_area_per(3, 4)

    # print_words(n, 'pippo', 'pluto', maiuscolo=True)


print(__name__)

if __name__ == '__main__':
    main()
