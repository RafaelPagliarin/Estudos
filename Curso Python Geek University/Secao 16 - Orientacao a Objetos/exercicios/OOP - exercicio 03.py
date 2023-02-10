class Elevador:

    def __init__(self, total_andares, capacidade):
        self.__andar_atual = 0
        self.__total_andares = total_andares
        self.__capacidade_maxima = capacidade
        self.__quantidade_atual = 0

    def entrar(self, valor):
        if self.__capacidade_maxima >= self.__quantidade_atual + valor:
            self.__quantidade_atual += valor
        else:
            print(f'Elevador em capacidade máxima, não é possível entrar.')

    def sair(self, valor):
        if self.__quantidade_atual - valor >= 0:
            self.__quantidade_atual -= valor
        else:
            print(f'Elevador vazio. Não há mais ninguém para sair do elevador')

    def subir(self, valor):
        self.__andar_atual = valor

    def descer(self, valor):
        self.__andar_atual = valor

    def get_andar_atual(self):
        return self.__andar_atual

    def get_quantidade_atual(self):
        return self.__quantidade_atual

    def set_andar(self, valor):
        if valor > self.__total_andares or valor < 0:
            print(f'Andar selecionado ({valor}) não existe')
        elif valor > self.__andar_atual:
            return self.subir(valor)
        elif valor < self.__andar_atual:
            return self.descer(valor)

    def set_pessoas(self, valor):
        if valor > 0:
            return self.entrar(valor)
        else:
            return self.sair(abs(valor))


casa = Elevador(20, 10)
print(f'{casa.get_quantidade_atual()} pessoas dentro do elevador, atualmente no {casa.get_andar_atual()} andar')

casa.set_andar(19)
casa.set_pessoas(5)
print(f'{casa.get_quantidade_atual()} pessoas dentro do elevador, atualmente no {casa.get_andar_atual()} andar')

casa.set_andar(14)
casa.set_pessoas(-2)
print(f'{casa.get_quantidade_atual()} pessoas dentro do elevador, atualmente no {casa.get_andar_atual()} andar')
