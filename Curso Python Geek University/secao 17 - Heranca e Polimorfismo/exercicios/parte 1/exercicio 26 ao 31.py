"""exercicio 26
    Escreva um código que apresente a classe Microondas, com atributo ligado e o método imprimir. O método imprimir
    deve mostrar na tela os valores de todos os atributos. O atributo ligado será boleano e deverá indicar o estado
    atual do microondas, se ligado ou desligado"""

"""exercicio 27
    Baseado no exercicio 26 adicione um método construtor que permita a definição de todos os atributos no momento
    da instanciação do objeto"""

"""exercicio 28
    Baseando-se no exercicio 27 adicone os métodos ligar e desligar que deverão mudar o conteúdo do atributo ligado
    conforme o caso"""

"""exercicio 29
    Baseando-se no exercicio 28 adicione o atributo portaFechada que deverá ser boleano e deverá indicar se a porta
    do microondas está ou não fechada. O método imprimir deve ser modificado de forma a mostrar na tela os valores de
    todos os atributos"""

"""exercicio 30
    Baseando-se no exercicio 29 adicione os métodos fecharPorta e abrirPorta que deverá mudar o conteúdo do atributo
    portaFechada conforme o caso"""

"""exercicio 31
    Basenado no exercicio 30 modifique o método ligar para que só ligue o equipamento quando a porta do mesmo estiver
    fechada, simulando assim o funcionamento do microondas."""


class Microondas:
    def __init__(self, ligado=False, porta_fechada=True):
        self.ligado = ligado
        self.porta_fechada = porta_fechada

    def imprimir(self):
        if self.ligado:
            print(f'O Microondas está ligado ', end='e ')
        else:
            print(f'O Microondas está desligado ', end='e ')

        if self.porta_fechada:
            print(f'a porta está fechada.')
        else:
            print(f'a porta está aberta')

    def ligar(self):
        if not self.ligado and self.porta_fechada:
            self.ligado = True
        if self.ligado:
            print('Já está ligado.')
        if not self.porta_fechada:
            print('Porta aberta, não é possível ligar.')

    def desligar(self):
        if self.ligado:
            self.ligado = False

    def fechar_porta(self):
        if not self.porta_fechada:
            self.porta_fechada = True

    def abrir_porta(self):
        if self.porta_fechada:
            self.porta_fechada = False


# Codewars
mi = Microondas()
mi.imprimir()
print()
mi.abrir_porta()
mi.imprimir()
print()
mi.desligar()
mi.imprimir()
print()
mi.ligar()
mi.imprimir()
print()
mi.fechar_porta()
mi.ligar()
mi.imprimir()