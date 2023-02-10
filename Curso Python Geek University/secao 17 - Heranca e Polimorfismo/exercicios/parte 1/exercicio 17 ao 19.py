"""
exercicio 17
    Escreva um código que apresente a classe Eletrodoméstico, com atributo ligado e o método imprimir. O método imprimir
    deve mostrar na tela os valores de todos os atributos. O atributo ligado será boleano e deverá indicar o estado
    atual do eletrodoméstico, se ligado ou desligado

exercicio 18
    Baseado no exercicio 17 adicione um método construtor que permita a definição de todos os atributos no momento
    da instanciação do objeto

exercicio 19
    Baseando-se no exercicio 18 adicone os métodos ligar e desligar que deverão mudar o conteúdo do atributo ligado
    conforme o caso
"""


class Eletrodomestico:
    def __init__(self, nome, ligado=False):
        self.nome = nome
        self.ligado = ligado

    def imprimir(self):
        print(f'O eletrodoméstico {self.nome} está ligado? {self.ligado}')

    def ligar(self):
        if not self.ligado:
            self.ligado = True
        else:
            print(f'{self.nome} já está ligado.')

    def desligar(self):
        if self.ligado:
            self.ligado = False
        else:
            print(f'{self.nome} já está desligado.')


eledo = Eletrodomestico('Torradeira')

eledo.imprimir()
eledo.ligar()
eledo.imprimir()