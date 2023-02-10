"""
Exercicio 1:
Escreva um código que apresente a classe Pessoa, com atributos nome, endereço e telefone e, o metodo imprimir.
O metodo imprimir deve mostrar na tela os valores de todos os atributos.

Exercicio 2:
Baseando-se no exericio 1, adicione um método construtor que permita a definição de todos os atributos no momento
da instanciação do objeto
"""


class Pessoa:
    def __init__(self, nome, endereco, telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone

    def imprimir(self):
        print(f'nome: {self.nome} \n'
              f'endereço: {self.endereco} \n'
              f'telefone: {self.telefone}')


rafael = Pessoa('Rafael', 'Rua das Baleias', '39449400')

rafael.imprimir()