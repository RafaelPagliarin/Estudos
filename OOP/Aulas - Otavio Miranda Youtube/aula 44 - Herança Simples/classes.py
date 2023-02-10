class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} está falando...')


class Cliente(Pessoa):
    def __init__(self, nome, idade, algo=None):
        super().__init__(nome, idade)
        self.algo = algo

    def comprar(self):
        print(f'{self.nomeclasse} está comprando')


class Aluno(Pessoa):
    def __init__(self, nome, idade, algo=None):
        super().__init__(nome, idade)
        self.algo = algo

    def estudar(self):
        print(f'{self.nomeclasse} está estudando')
