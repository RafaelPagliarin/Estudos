from datetime import date


class Pessoa:
    def __init__(self, nome=None, ano_nascimento=0, altura=None):
        self.__nome = nome
        self.__idade = date.today().year - ano_nascimento
        self.__altura = altura

    def pegar_nome(self, nome):
        self.__nome = nome

    def pegar_nascimento(self, nascimento):
        self.__idade = date.today().year - nascimento

    def pegar_altura(self, altura):
        self.__altura = altura

    def mostrar_pessoa(self):
        print(f'{self.__nome} tem {self.__idade} anos e {self.__altura}cm de altura')


pessoa1 = Pessoa('Rafael', 1992, 183)

pessoa1.mostrar_pessoa()

pessoa2 = Pessoa()

pessoa2.pegar_nome('Bárbara')
pessoa2.pegar_nascimento(1993)
pessoa2.pegar_altura(170)

pessoa2.mostrar_pessoa()


