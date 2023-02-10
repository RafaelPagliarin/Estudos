"""

OOP - Polimorfismo

poli = muitos
morfis = formas

Objetos que podem possuir muitas formas

Overriding => é a essencia da representação do polimorfismo.

"""


class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        raise NotImplementedError('A classe filha precisa implementar este método')

    def comer(self):
        print(f'{self.nome} está comendo...')


class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self.nome} fala auw auw')


class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self.nome} fala miau')


class Rato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self.nome} fala algo...')


# Codewars
felix = Gato('Felix')
felix.falar()
felix.comer()

pluto = Cachorro('Pluto')
pluto.falar()
pluto.comer()

mickey = Rato('Michey')
mickey.falar()
mickey.comer()
