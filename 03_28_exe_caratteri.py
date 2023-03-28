


output = input("Stringa")
# output = v[0] + v[1] + v[2] + "..." + v[-3] + v[-2] + v[-1]


if len(output) > 6:
    output = output[0:3] + "..." + output[-3:]

print(output)
