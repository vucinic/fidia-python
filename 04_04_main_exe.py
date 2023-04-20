"""
- chiede numero carta all'utente
- recupera indice carta
- recupera pin corrispondete
- chiede input pin
- confronta fino a N max tentativi
- se ok prima di N stampa pin corretto
- se ko dopo N stampa carta bloccata
- quando a finito con l' utente corrente ritorna in attesa di un nuovo utonto
 (chiede n carta)
"""
MAX_ATTEMPTS = 3

carte = [
    '123456',
    '123457',
    '123458',
    '123459',
]
pin = [
    '11111',
    '22222',
    '33333',
    '44444',
]

while (c := input('---- NUOVO UTENTE ---------\nNumero carta')) != '##exit##':

    if c in carte:

        pin_index = carte.index(c)

        pin_correct = pin[pin_index]

        count_attempts = 0
        is_correct = False

        while count_attempts < MAX_ATTEMPTS and not is_correct:
            attempt = input('\t+ Inserire pin: ', )
            is_correct = attempt == pin_correct
            if not is_correct:
                print('\t- Pin errato')

            count_attempts += 1

        if is_correct:
            print("\t+ Pin corretto")
        else:
            print("\t- Carta bloccata")

    else:
        print('\t- Carta inesistente')

    print("---------------------------")
    print()


