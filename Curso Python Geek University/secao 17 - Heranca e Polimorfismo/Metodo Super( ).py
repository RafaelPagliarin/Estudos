"""
O Método super()

se refere a super classe (usado para apontar hierarquias)

"""


class Animal:
    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f'O(A) {self.__nome} faz {som}')


class Gato(Animal):
    def __init__(self, nome, especie, raca):
        super().__init__(nome, especie)
        self.__raca = raca


ya = Gato('Ya', 'Felino', 'Sem raça definida')

ya.faz_som('miau')