import traceback


f_out = open('ciccio', 'w')
list_a = [4, 5, 3, 4, 5, 6, 6]


try:
    #
    #
    #
    print('Errore prima divisione ')
    raise OSError()

except OSError as e:
    print(traceback.format_exc())
