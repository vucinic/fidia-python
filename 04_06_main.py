t = (3, 4, 5, 6, 6)
l = [1, 4, 5, 6, 6]

tuple_l = (l)

intero = int()
sq1 = list(i ** 2 for i in l)
sq2 = [i ** 2 for i in l]
sq3 = tuple(i ** 2 for i in l)

generatore = (i ** 2 for i in l)

list_da_gen = list(generatore)
list_da_gen0 = list(generatore)
list_da_gen1 = list(list_da_gen)
list_da_gen2 = list(i ** 2 for i in l)
list_da_gen3 = list(i ** 2 for i in l)

for elem in [i ** 2 for i in l]:
    print(elem)

p = sq1[1]
print(p)

sq2 = [i ** 2 for i in l if (i % 2 == 0 and i > 0)]


def f_get():
    for i in range(100):
        print('f_get', i)
        yield i


# for z in f_get():
#     print('got', z)

for z in generatore:
    print('got', z)

# sp2 = []
# for i in l:
#     if i % 2 == 0:
#         sp2.append(i ** 2)


righe = 'ABCD'
cols = '1234'

res = []
for r in righe:
    for c in cols:
        if r != 'A' and c != '2':
            res.append(r + c)
print(res)

res = tuple(r + c for r in righe for c in cols if r != 'A' and c != '2')
print(res)

t = [[0] * 3] * 3

t1 = [
    [0, 1, 2],
    [0, 1, 2, 5],
    [0, 1, 2],
    [0] * 3
]
RIGHE = 4
COLONNE = 3

for r in range(RIGHE):
    for c in range(COLONNE):
        t1[r][c] = -1
        print(t1[r][c], end=' ')
    print()

print('------')
for r in t1:
    for c in r:
        print(c, end=' ')
    print()

t = [[0] * 5] * 3

t1 = [
    [],
    [],
    [],
    []
]

print()

set1 = {'red', 'blue', 'green'}
set2 = {'red', 'white', 'green'}

set_res = set1.union(set2).difference(set1.intersection(set2))
print(*(f"'{i}'" for i in set_res))

set_res = set1.symmetric_difference(set2)
print(set_res)

dizionario = {
    'alessio': [34, 'Via rossi', 56],
    'mario': {
        'eta': 34,
        'indirizzo': {
            'via': 'Via rossi',
            'civico': 56
        },
        'lista_voti': [24, 23, 18]
    },
    'luiginio': 8
}

dizionario['beppe'] = 98

print(dizionario['mario']['indirizzo']['via'])
# print(dizionario['mario']['casa']['via'])
print(dizionario.get('mario', {}).get('indirizzo', {}).get('via', {}))
print('--->', dizionario.get('mario', {}).get('casa', {}).get('via', {}))
print(dizionario['alessio'][1])

for key in sorted(dizionario):
    print(key, '->', dizionario[key])

print(' --------- ')

for item in dizionario.items():
    print(item[0], '->', dizionario[item[0]])

    print(item[0], '->', item[1])
print(' --------- ')

for (key, val) in dizionario.items():
    print(key, '->', val)

print(' --------- ')
