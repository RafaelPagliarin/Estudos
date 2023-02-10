"""
OOP - Abstração e Encapsulamento


O grande objetivo da OOP é encapsular o nosso código dentro de um grupo lógico e hierarquico utilizando classes.

Encapsular -> capsula


# Relembrando Atributos/Métodos privados em Python

Imagine que temos uma classe chamada Pessoa, contendo um atributo privado chamado __nome e um método privado chamado
__falar()

Esses elementos privados só deveriam ser acessados dentro da classe. Porém o Python não impede o acesso fora dela.
Em Python existe um fenomeno chamado 'Name Mangling' que faz uma alteração na forma de se acessar elementos privados.

_Classe__elemento

Exemplo:

instancia._Pessoa__nome
instancia._Pessoa__falar()


Abstração, em OOP, é o ato de expor apenas dados relevantes de uma classe, escondendo atributos e métodos privados do
usuário.

"""


class Conta:
    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        self.__valor += valor

    def sacar(self, valor):
        self.__saldo -= valor

#testando


conta1 = Conta('Rafael', 140, 4000)

print(conta1.__dict__)

print(conta1.numero)
print(conta1.titular)
print(conta1.saldo)
print(conta1.limite)