"""
Exercicio 3:
Escreva um código que apresente a classe Quadrado, com atributos lado, área e perímetro e, os metodos calcularArea,
calcularPerimetro devem efetuar seus respectivos cálculos e colocar os valores nos atributos area e perimetro.
O metodo imprimir deve mostrar na tela os valores de todos os atributos. Salienta-se que a área de um quadrado é obtida
pela fórmula (lado * lado) e o perímetro por (4 * lado).

Exercicio 4:
Baseando-se no exercício 3 adicione um método construtor que permita a definição de todos os atributos no momento
da instanciação do objeto.
"""


class Quadrado:
    def __init__(self, lado, area=None, perimetro=None):
        self.lado = lado
        self.area = area
        self.perimetro = perimetro

    def calcular_area(self):
        self.area = self.lado * self.lado

    def calcular_perimetro(self):
        self.perimetro = self.lado * 4

    def imprimir(self):
        print(f'O quadrado de lado {self.lado}, possui area de {self.area} e perimetro de {self.perimetro}')


quad = Quadrado(3)

quad.calcular_area()
quad.calcular_perimetro()
quad.imprimir()

