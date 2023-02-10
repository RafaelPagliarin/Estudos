"""
exercicio 9
    Escreva um código que apresente a classe Moto, com atributos marca, modelo, cor e marcha, e o método imprimir.
O metodo imprimir deve mostrar na tela os valores de todos os atributos. o atributo marcha indica em que marcha a
Moto se encontra no momento, sendo representado de forma inteira, onde 0 - neutro, 1 - primeira, etc

exercicio 10
    Baseando-se no exercicio 9 adicione um método construtor que permita a definição de todos os atributos no momento da
instanciação do objeto

exercicio 11
    Baseandos-se no exericio 10 adicione os métodos marchaAcima e marchaAbaixo que deverão efetuar a troca de marcha

exercicio 12
    Baseando-se no exercicio 11 adicione os atributos menorMarcha e maiorMarcha. Desta forma os métodos subir_marcha e
descer_marcha devem ser reescritos de forma a não permitirem a troca de marchas para valores acima ou abaixo dos atributos

exercicio 13
    Baseando-se no exercício 12 adicione um método construtor que permita a definição de todos os atributos no momento da
instanciação do objeto

exercicio 14
    Baseando-se no exercicio 13 adicione o atributo ligada que terá a função de indicar se a moto está ligada ou não.
Esse atributo deve ser do tipo boleano. O método imprimir deve ser modificado de forma a mostrar os novos atributos

exercicio 15
    Baseando-se no exercício 14 adicione um método construtor que permita a definição de todos os atributos no momento da
instanciação do objeto

exercicio 16
    Baseando-se no exericio 15 adicione os metodos ligar e desligar que deverão mudar o conteúdo do atributo ligada
conforme o caso
"""


class Moto:
    def __init__(self, marca, modelo, cor, menor_marcha, maior_marcha, marcha=0, ligada=False):
        self.__marca = marca
        self.__modelo = modelo
        self.__cor = cor
        self.__menor_marcha = menor_marcha
        self.__maior_marcha = maior_marcha
        self.__marcha = marcha
        self.__ligada = ligada

    def subir_marcha(self):
        if self.__marcha + 1 <= self.__maior_marcha and self.__ligada:
            self.__marcha += 1
        else:
            print('Já está na maior marcha ou está desligada')

    def descer_marcha(self):
        if self.__marcha - 1 >= self.__menor_marcha and self.__ligada:
            self.__marcha -= 1
        else:
            print('Já está na menor marcha ou está desligada')

    def ligar(self):
        if not self.__ligada:
            self.__ligada = True
        else:
            print('Moto já está ligada')

    def desligar(self):
        if self.__ligada:
            self.__ligada = False
            self.__marcha = 0
        else:
            print('Moto já está desligada')

    def imprimir(self):
        print(f'Moto: {self.__modelo}, cor: {self.__cor}, marca: {self.__marca}, '
              f'menor marcha: {self.__menor_marcha} e maior marcha: {self.__maior_marcha}', end=', ')
        if self.__ligada:
            print(f'encontra-se ligada na marcha {self.__marcha}')
        if not self.__ligada:
            print(f'encontra-se desligada')


# Codewars
harley = Moto('Harley', 'Breakout', 'Preto', 0, 6)

harley.imprimir()
harley.ligar()
harley.subir_marcha()
harley.subir_marcha()
harley.subir_marcha()
harley.imprimir()
print()
harley.descer_marcha()
harley.imprimir()
print()
harley.desligar()
harley.imprimir()

