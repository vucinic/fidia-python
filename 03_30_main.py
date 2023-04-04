#
#
# # v = input("Valore")
# i = 0
# #
# data = ''
#
# while (v := input("Valore")) != '$':
#
#     if v != 'u':
#         data = data + v
#
# print(f'Messaggio:\n\t{data[:-1]}')
#

letter = 'c'
stringa = 'pippo'

# [i for i in stringa if i not in 'aeiou']
# for x in stringa[:-2]:
for x in range(1, len(stringa), 2):
    print(stringa[x])
    if stringa[x] in 'aeiou':
        print(f"Vocale in posizione {x}")

print()

for (x, letter) in enumerate(stringa):
    print(f"{x}: {letter}")

print()
for (x, letter) in enumerate(range(5)):
    print(f"{x}: {letter}")

print()

i = 0
while i < len(stringa):
    letter = stringa[i]
    print(letter)
    i = i + 1

print(letter)
