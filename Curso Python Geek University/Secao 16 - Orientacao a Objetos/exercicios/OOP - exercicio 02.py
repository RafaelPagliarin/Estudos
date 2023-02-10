class Agenda:
    counter = 0
    lista_agenda = []

    def __init__(self):
        self.__lista = []

    def armazenar_pessoa(self, nome, idade, altura):
        pessoa = [nome, idade, altura]
        if len(self.__lista) < 10:
            self.__lista.append(pessoa)
        else:
            print(f'Lista já possui 10 contatos armazenados.')

    def remover_pessoa(self, nome):
        for chave, valor in enumerate(self.__lista):
            if valor[0] == nome:
                self.__lista.pop(chave)

    def buscar_pessoa(self, nome):
        for chave, valor in enumerate(self.__lista):
            if valor[0] == nome:
                print(f'Pessoa encontra-se na posição: {chave+1} da agenda.')

    def imprimir_agenda(self):
        for chave, valor in enumerate(self.__lista):
            print(f'Nome: {valor[0]}, idade: {valor[1]} anos, altura: {valor[2]}cm')

    def imprimir_pessoa(self, index):
        for chave, valor in enumerate(self.__lista):
            if index == chave:
                print(f'Nome: {valor[0]}, idade: {valor[1]} anos, altura: {valor[2]}cm')




teste = Agenda()

teste.armazenar_pessoa('Rafael', 30, 183)
teste.armazenar_pessoa('Bárbara', 29, 170)
teste.armazenar_pessoa('Anita', 9, 25)

teste.imprimir_agenda()
teste.buscar_pessoa('Rafael')
teste.remover_pessoa('Rafael')
teste.imprimir_pessoa(0)


