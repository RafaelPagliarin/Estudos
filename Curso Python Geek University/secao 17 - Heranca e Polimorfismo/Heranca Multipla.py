"""
OOP - Herança Múltipla

Nada mais é do que a possibilidade de uma classe herdar de multiplas classes. fazendo com que a classe filha herde
todos os atributos e métodos das classes herdadas

obs: pode ser feita de duas maneiras:
    - por multiderivação direta
    - por multiderivação indireta

# Exemplo 1 - Multiderivação Direta
class Base1:
    pass

class Base2:
    pass

class Base3:
    pass

class MultiDerivada(Base1, Base2, Base3):
    pass

# Exemplo 2 - Multiderivação Indireta
class Base1:
    pass

class Base2(Base1):
    pass

class Base3(Base2):
    pass

class MultiDerivada(Base3):
    pass
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


class Pinguim(Terrestre, Aquatico):
    def __init__(self, nome):
        super().__init__(nome)


# Testando
baleia = Aquatico('Wally')
print(baleia.nadar())
print(baleia.cumprimentar())
print()
tatu = Terrestre('Shin')
print(tatu.andar())
print(tatu.cumprimentar())
print()
pg = Pinguim('Jhonny')
print(pg.andar())
print(pg.nadar())
print(pg.cumprimentar()) #??? Como ele herdou primeiro o Terrestre, ele executará o method do terrestre Method Resolution Order - MRO -

# Objeto é instancia de

print(f'Tux é instancia de Pinguim? {isinstance(pg, Pinguim)}')
print(f'Tux é instancia de Aquatico? {isinstance(pg, Aquatico)}')
print(f'Tux é instancia de Terrestre? {isinstance(pg, Terrestre)}')
print(f'Tux é instancia de object {isinstance(pg, object)}')