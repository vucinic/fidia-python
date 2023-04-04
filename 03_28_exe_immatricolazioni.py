m1 = input('Matricola 1: ')
m2 = input('Matricola 2: ')

valid = True

# region Checks...
if m1[1:].isdigit() == False:
    print(f'Matricola 1 non valida: {m1}')
    valid = False

if not m2[1:].isdigit():
    print(f'Matricola 2 non valida: {m2}')
    valid = False
# endregion

if valid:

    if int(m1[1:]) > int(m2[1:]):
        print(m2, m1)
    else:
        print(m1, m2)
