import random

dat
class Persona:
    tot_persone = 0

    def __init__(self, nome: str, eta=25):
        Persona.tot_persone += 1
        self.nome = nome
        self.eta = eta
        self.__super_private = random.randint(0, 1_000_000)

class Persona:
    tot_persone = 0

    def __init__(self, nome: str, eta=25):
        Persona.tot_persone += 1
        self.nome = nome
        self.eta = eta
        self.__super_private = random.randint(0, 1_000_000)

    def __str__(self) -> str:
        self.altezza = 324

        return f"Ciao, il mio nome è {self.nome} e ho {self.eta} anni."

    def getEta(self, p: str) -> int:
        return self.eta

    def set(self, **par):
        for (k, v) in par.items():
            self.__dict__[k] = v

    def saluto(self):
        print(f"Ciao, il mio nome è {self.nome} e ho {self.eta} anni.")


var = str()
# print(f'Esistono {Persona.tot_persone} persone')


variabile = Persona(eta=25, nome=23 ) #"Mario")
print(f'Esistono {Persona.tot_persone} persone')

variabile2 = Persona("Carlo")
# print(f'Esistono {Persona.tot_persone} persone')

variabile.saluto()
variabile2.saluto()

variabile2.set(nome='Michela', eta=27, altezza="175")

if isinstance(variabile2, Persona):
    print('str')
else:
    print('nostr...')

str(variabile)


variabile2.getEta(234)

