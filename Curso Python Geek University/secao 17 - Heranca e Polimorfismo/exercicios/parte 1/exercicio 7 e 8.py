"""
Exercicio 7:
Escreva um código que apresenta a classe Circulo, com atributos raio, área e perimetro e os métodos calcularArea,
calcularPerimetro e imprimir. Os métodos calcularArea e calcular Perimetro devem efetuar seus respectivos calculos
e colocar os valores nos atributos area e perimetro. O método imprimir deve mosntrar na tela os valores de todos os
atributos. Salienta-se que a área de um circulo é obtida pela formula (pi * raio * raio) e o perímetro por
(2 * pi * raio), onde pi = 3,1415

Exercicio 8:
Baseando-se no exercício 7 adicione um método construtor que permita a definição de todos os atributos no momento da
instanciação do objeto
"""
from math import pi


class Circulo:
    def __init__(self, raio, area=None, perimetro=None):
        self.raio = raio
        self.area = area
        self.perimetro = perimetro

    def calcular_area(self):
        self.area = pi * self.raio ** 2

    def calcular_perimetro(self):
        self.perimetro = 2 * pi * self.raio

    def imprimir(self):
        print(f'O circulo de raio {self.raio} possui área de {round(self.area, 2)} e perímetro de'
              f' {round(self.perimetro, 2)}')


cir = Circulo(6)

cir.calcular_perimetro()
cir.calcular_area()

cir.imprimir()
