"""
OOP - MRO - Method Resolution Order

é a ordem de execução dos métodos (quem será executado primeiro).

em Python, podemos conferir a execução dos métodos (MRO) em 3 formas:
    - via propriedade da classe __mro__
        - print(Pinguim.__mro__)

    - via metodo mro()
        - print(Pinguim.mro())

    - via help
        - help(Pinguim)



"""


class Animal:
    def __init__(self, nome):
        self.nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.nome}'


class Aquatico(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self.nome} está nadando.'

    def cumprimentar(self):
        return f'Eu sou {self.nome} do mar.'


class Terrestre(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self.nome} está andando.'

    def cumprimentar(self):
        return f'Eu sou {self.nome} da terra.'


class Pinguim(Aquatico, Terrestre):
    def __init__(self, nome):
        super().__init__(nome)


# Testando
pg = Pinguim('Jhonny')
print(pg.cumprimentar())
# Como ele herdou primeiro o Terrestre, ele executará o method do terrestre

"""
Logo a ordem de hierarquia importa:

Pinguim(Terrestre, Aquatico)
Eu sou Jhonny da terra.

Pinguim(Aquatico, Terrestre)
Eu sou Jhonny do mar.
"""

print(Pinguim.__mro__)

print(Pinguim.mro())

help(Pinguim)

