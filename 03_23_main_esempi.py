#
#
#
# msg = "0123456789ABCDEFGHILMN"
#
# char = msg[8]
#
# v = 3.14
# print("'", msg[5:12:1], "'", sep="")
# print("'", msg[5:12:-1], "'", sep="")
#
#
# print('-->', chr(0x1f600), ord('€'))
#
#
# print("'", msg[12:5], "'", sep="")
# print("'", msg[::-1], "'", sep="")


# print(msg[5:-4])
# print(msg[:-4])
# print(msg[5:])
# print(msg[:])


# print(msg + " " + v)
# print(str(msg) + " " + str(v))
# print(msg, v)
#
# print(msg[0])
# print(msg[len(msg) - 1])
# print(msg[-len(msg)])
#
#

format = 'Hello numero "%15.2f" "%f" '
format = 'Hello numero "{primo_par}" "{c}" '


n = 32.12
print(f'Ciao numero 0x"{int(n if n > 10 else 45):<10x}"')
print(f'Ciao numero "{n:a<010}"')
print(f'Ciao numero "{n:15f}"')

print('Hello numero "%15.2f" "%f" ' % (n, n))

str_1 = f'Ciao numero "{n:a<010}"'

format = 'Hello numero "{primo_par}" "{c}" '
print(format.format(primo_par="ciao", c="zio"))

print(float(f'{n:.3f}'))
