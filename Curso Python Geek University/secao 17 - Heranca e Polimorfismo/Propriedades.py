"""
POO - Propriedades / Properties

PS: em linguagens de programação como o Java, ao declararmos atributos privados nas classes, costumamos criar métodos
publicos para manipular esses atributos. Esses metodos são conhecidos como getters e setters, onde os getters retornam
o valor do atributo e os setters alterarm o valor do atributo
########################################################################################################################
class Conta:
    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def set_titular(self, titular):
        self.__titular = titular

    def set_limite(self, limite):
        self.__limite = limite


conta1 = Conta('Rafael', 3000, 5000)
conta2 = Conta('Bárbara', 4000, 8000)

print(conta1.extrato())
print(conta2.extrato())

soma = conta1.get_saldo() + conta2.get_saldo()
print(f'A soma dos saldos das contas é {soma}')

print(conta1.__dict__)
conta1.set_limite(10000000)
print(conta1.__dict__)
########################################################################################################################


quando usamos o decorator @property ele considera que a função é um getter, para usar um setter precisamos usar outro
decorator chamado @nome.setter


class Conta:
    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, novo_saldo):
        self.__saldo = novo_saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor


conta1 = Conta('Rafael', 3000, 5000)
conta2 = Conta('Bárbara', 4000, 8000)

print(conta1.extrato())
print(conta2.extrato())

soma = conta1.saldo + conta2.saldo
print(f'A soma dos saldos das contas é {soma}')

print(conta1.__dict__)
conta1.limite = 100000
print(conta1.__dict__)
"""

