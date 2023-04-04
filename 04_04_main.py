#
# POWER = 2
#
# max_n = int(input("max"))
#
# l = []
# for n in range(max_n):
#     l.append(n**POWER)
#     # l += [n*n]
#     # l += [n**2]
#
# print(l)
# print([i**POWER for i in range(max_n)])

nomi = [
    'mario',
    'piero',
    'mimmo'
]
print(nomi)
'mario, piero, mimmo'

res = ''
for (i, nome) in enumerate(nomi):
    res += nome
    if i != len(nomi) - 1:
        res += ', '
print(res)

res = ''
for nome in nomi[:-1]:
    res += nome + ', '

res += nomi[-1]
print(res)

res = ''
for nome in nomi:
    res += nome + ', '

res = res[:-2]
print(res)

res = ', '.join(nomi)
print(res)

res = str(nomi)
res = res.replace("'", "").replace('[', '').replace(']', '')
print(res)
# resto del mondo si, qui no
# nomi.join(', ')


_in = 'Maria,Rossi,10,03,65'.split(',')
print(_in)

stringhe = [
    'mar',
    'mario',
    'maria',
    'mari',
    'mario',
    'mao',
    'po',
    'mdsdso'
]

i = 0
while i < len(stringhe):
    if len(stringhe[i]) < 4:
        stringhe.pop(i)
    else:
        i += 1
print(stringhe)

res = []
for el in stringhe:
    if len(el) >= 4:
        res.append(el)
print(res)

tmp = stringhe[-1]
stringhe[-1] = stringhe[0]
stringhe[0] = tmp
print(stringhe)

stringhe[-1], stringhe[0] = stringhe[0], stringhe[-1]

print(stringhe)

pippo = 3
pluto = 4

stringhe[-1], stringhe[0] = pluto, pippo
print(stringhe)

print([i for i in enumerate(nomi)])

p, q = [3, 4]
print(p, q)
