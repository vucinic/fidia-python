import os

if os.path.exists("output.dat"):
    print('File exists')
    os.rename("output.dat", "output.dat.bak")


with open("output.dat", 'w+b') as f:
    f.write(bytes('ciao\n'.encode('utf-8')))

    bb = 0x32_45_56_45_45_3F_FF_02.to_bytes(12, 'little')
    print([f'{i:02X}' for i in bb])
    print(bb)
    bb = 0x32_45_56_45_45_3F_FF_02.to_bytes(12, 'big')
    print('_'.join([f'{i:02X}' for i in bb]))

    # f.write()



    # f.writelines(
    #     list((i + '\n') for i in ['mamma', 'guarda', 'come', 'mi diverto'])
    # )

    # print('Ciao', file=f)


    # print(st)
