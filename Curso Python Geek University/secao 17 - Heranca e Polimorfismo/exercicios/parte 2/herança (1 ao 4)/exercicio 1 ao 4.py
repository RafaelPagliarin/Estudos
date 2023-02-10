""" 1. Crie um novo pacote com o nome herança (1 ao 4). Todas as três (3) classes criadas abaixo deverão ser salvas
       nesse pacote

    2. Crie uma classe Equipamentos com dois atributos privados.

    3. Crie uma classe Computador com dois atributos à sua escolha, também privados. A classe Computador deverá herdar
       tudo da classe Equipamentos

    4. Crie os métodos de acesso e de modificação para os atributos definidos em ambas as classes."""


class Equipamento:
    def __init__(self, voltagem, id_equip):
        self.__voltagem = voltagem
        self.__id_equip = id_equip

    @property
    def voltagem(self):
        return self.__voltagem

    @voltagem.setter
    def voltagem(self, novo):
        self.__voltagem = novo

    @property
    def id_equip(self):
        return self.__id_equip

    @id_equip.setter
    def atri2(self, novo):
        self.__id_equip = novo

    def exibe(self):
        print(f'Voltagem: {self.__voltagem}\nID: {self.__id_equip}')


class Computador(Equipamento):
    def __init__(self, voltagem, id_equip, os, memoria):
        super().__init__(voltagem, id_equip)
        self.__os = os
        self.__memoria = memoria

    @property
    def os(self):
        return self.__os

    @os.setter
    def os(self, novo):
        self.__os = novo

    @property
    def memoria(self):
        return self.__memoria

    @memoria.setter
    def memoria(self, novo):
        self.__memoria = novo

    def exibe(self):
        print(f'Voltagem: {self._Equipamento__voltagem}\nID: {self._Equipamento__id_equip}')
        print(f'OS: {self.__os}\nMemória: {self.__memoria}')


""" 5. Crie uma classe TestaEquipamento, que deverá conter o método main(), crie nela um objeto da classe Equipamento
       e instancie os dois atributos que você declarou na classe Equipamento. Crie também um objeto da classe Computador
       utilizando os dois atributos declarados na própria classe e os dois herdados da classe Equipamento.

    6. O método main() deve exibir as informações dos dois objetos criados.

    7. Criar o método exibe() na classe Equipamento para mostrar os dados dessa classe.

    8. Reescreva o método exibe() na classe Computador, aproveitando o que já foi escrito na superclasse Equipamento

"""


class TestaEquipamento:
    def __init__(self):
        self.__equip = Equipamento(220, 'EXN4945')
        self.__cpu = Computador(220, 'CPU_Raizen', 'Windows', '32 GB')
        print(self.__dict__)

    def main(self):
        print('Equipamento:')
        self.__equip.exibe()
        print("\nComputador")
        self.__cpu.exibe()


# Codewars

teste = TestaEquipamento()
teste.main()