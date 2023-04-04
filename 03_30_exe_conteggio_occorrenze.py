da_censurare = input('Stringa da censurare: ')
caratteri = input('Caratteri proibiti: ')

# region Sol 1
count = 0
for c in da_censurare:
    if c.lower() in caratteri.lower():
        print('*', end='')
        count = count + 1
    else:
        print(c, end='')

print()
print(f'{count} caratteri sostituiti')
# endregion

# region Sol 2
output = ''
count = 0
for c in da_censurare:
    if c.lower() in caratteri.lower():
        output += '*'
        count = count + 1
    else:
        output += c

print(output)
print(f'{count} caratteri sostituiti')
# endregion

output = ''
count = 0
for c in da_censurare:
    trovato = False
    i = 0
    while not trovato and i < len(caratteri):
        if c == caratteri[i]:
            trovato = True
        i += 1

    # if trovato:
    #     count += 1
    #     output = output + '*'
    # else:
    #     output = output + c

    output += c if not trovato else '*'
    count += int(trovato)

print(output)
print(f'{count} caratteri sostituiti')

output = da_censurare
for c in caratteri:
    output = output.replace(c, '*')

print(output)

# qui prendo da_censurare e gli sostutisco ogni occorrenza di caratteri con un *
print(''.join([c if c not in caratteri else '*' for c in da_censurare]))


