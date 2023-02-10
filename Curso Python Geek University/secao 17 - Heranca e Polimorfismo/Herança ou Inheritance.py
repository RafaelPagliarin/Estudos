"""
POO - Herança (Inheritance)

A ideia de herança (1 ao 4) é a de reaproveitar código. Também extender nossas classes.

obs: com a herança (1 ao 4) a partir de uma classe existente, nós extendemos outra classe que passa a herdar atributos e metodos
da classe herdada.

exemplo: imagine um banco com as seguintes classes

Cliente
    - nome
    - sobrenome
    - cpf
    - renda

Funcionario
    - nome
    - sobrenome
    - cpf
    - matricula


Existe alguma entidade genérica suficiente para encapsular os atributos e métodos comuns a outras entidade?
Se você notar, ambos possuiem 3 atributos identicos e um metodo.

##############################################################################################################
class Cliente:
    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Funcionario:
    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


cliente1 = Cliente('Rafael', 'Pagliarin', '41142963870', 50000)
func1 = Funcionario('Barbara', 'Trifler', '43459874150', 1234)
print(cliente1.nome_completo())
print(func1.nome_completo())
##############################################################################################################

Quando uma classe herda outra classe, ela herda TODOS os atributos e métodos da classe herdada

quando uma classe herda de outra classe, a classe herdada é conhecida como:
- super classe
- classe mae
- classe pai
- classe base
- classe generica

quando uma classe herda de outra classe, ela é conhecida como:
- sub classe
- classe filha
- classe específica

##############################################################################################################
class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, cpf , renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula


cliente1 = Cliente('Rafael', 'Pagliarin', '41142963870', 50000)
func1 = Funcionario('Barbara', 'Trifler', '43459874150', 1234)
print(cliente1.nome_completo())
print(func1.nome_completo())
##############################################################################################################

# Sobrescrita de Métodos (Overriding)
# Ocorre quando reescrevemos um método presente na superclasse em classes filhas

class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'


class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, cpf , renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def nome_completo(self):
        return f'Funcionário: {self.__matricula} Nome: {self.nome} {self.sobrenome}'


cliente1 = Cliente('Rafael', 'Pagliarin', '41142963870', 50000)
func1 = Funcionario('Barbara', 'Trifler', '43459874150', 1234)
print(cliente1.nome_completo())
print(func1.nome_completo())
"""

##############################################################################################################


##############################################################################################################

