"""
JSON e Pickle

JSON -> JavaScript Object Notation

é um tipo de arquivo super comum em API's.

==========================================================================================
import json

retorno = json.dumps(['produto', {'playstation 4': ('2TB', 'Novo', '220v', 2340)}])

print(type(retorno))

print(retorno)
"""

import json

class Gato:
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato('Felix', 'SRD')

"""print(felix.__dict__)

ret = json.dumps(felix.__dict__)

print(ret)"""


# integrando o JSON com Pickle
# pip instal jsonpickle

import jsonpickle

# Escrevendo arquivo json/pickle
"""with open('felix.json', 'w') as arquivo:
    ret = jsonpickle.encode(felix)
    arquivo.write(ret)"""

# Lendo arquivo json/pickle
with open('felix.json', 'r') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(type(ret))
    print(ret.nome)
    print(ret.raca)
