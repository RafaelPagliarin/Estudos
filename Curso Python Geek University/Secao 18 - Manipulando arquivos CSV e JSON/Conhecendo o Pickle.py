"""
Conhecendo o Pickle

função do pickle é realizar o seguinte processo:
 objeto python -> binarização
 objeto binarizado -> objeto python

esse processo é chamado de serialização/deserialização

obs: o módulo Pickle não é seguro contra dados maliciosos e desta forma não é recomendado trabalhar com arquivos
pickle vindo de outras pessoas que você não conheça ou de fontes desconhecidas.

"""
import pickle


class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def comer(self):
        print(f'{self.__nome} está comendo...')

    @property
    def nome(self):
        return self.__nome


class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def miar(self):
        print(f'{self.nome} está miando...')


class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def latir(self):
        print(f'{self.nome} está latindo...')


"""felix = Gato('Felix')
pluto = Cachorro('Pluto')

# Fazendo a escrita em arquivos Pickle:

with open('animais.pickle', 'wb') as arquivo:
    pickle.dump((felix, pluto), arquivo)"""

# Fazendo a leitura de dados em arquivos Pickle

with open('animais.pickle', 'rb') as arquivo:
    gato, cachorro = pickle.load(arquivo)
    print(f'O gato chama-se {gato.nome}')
    gato.miar()
    print(f'O tipo do gato é {type(gato)}')
    print()
    print(f'O cachorro chama-se {cachorro.nome}')
    cachorro.latir()
    print(f'O tipo do cachorro é {type(cachorro)}')