"""
Exercicio 5:
Escreva um código que apresente a classe Retângulo, com atributos comprimento, largura, área e perímetro e, os metodos
calcularArea, calcularPerimetro e imprimir. Os métodos calcularArea e calcularPerimetro devem efetuar seus respectivos
calculos e colocar os valores nos atributos area e perimetro. O método imprimir deve mostrar na tela os valores de todos
os atributos. Salienta-se que a área de um retângulo é obtida pela fórmula (comprimento * largura) e o perimetro por
(2 * comprimento) + (2 * largura)

Exercicio 6:
Baseando-se no exercicio 5 adicione um método construtor que permita a definição de todos os atributos no momento
da instanciação do objeto.
"""


class Retangulo:
    def __init__(self, comprimento, largura, area=None, perimetro=None):
        self.comprimento = comprimento
        self.largura = largura
        self.area = area
        self.perimetro = perimetro

    def calcular_area(self):
        self.area = self.comprimento * self.largura

    def calcular_perimetro(self):
        self.perimetro = (self.comprimento * 2) + (self.largura * 2)

    def imprimir(self):
        print(f'O retangulo de largura {self.largura} e comprimento {self.comprimento} possui área de {self.area}'
              f' e perimetro de {self.perimetro}')


ret = Retangulo(10, 5)

ret.calcular_area()
ret.calcular_perimetro()
ret.imprimir()