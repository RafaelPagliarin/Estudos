"""exercicio 20
    Escreva um código que apresente a classe Televisor, com atributos ligado, canal e volume, e o método imprimir.
    O metodo imprimir deve mostrar na tela os valores de todos os atributos. O atributo ligado será boleano e deverá
    indicar o estado atual do televisor, se ligado ou desligado. O atributo canal deverá indicar o canal atual em que
    o televisor está sintonizado. O atributo volume indicará o volume atual do televisor"""

"""exercicio 21
    Baseado no exercicio 20 adicione um método construtor que permita a definição de todos os atributos no momento
    da instanciação do objeto"""

"""exercicio 22
        Baseando-se no exercicio 21 adicone os métodos ligar e desligar que deverão mudar o conteúdo do atributo ligado
    conforme o caso"""

"""exercicio 23
    Baseando-se no exercicio 22 adicione os atributos numeroCanais e, volumeMaximo, onde numeroCanais indica o número
    máximo de canais que o televisor pode sintonizar e volumeMaximo indica qual o maior nível de volume possível.
    O método imprimir deve ser modificado de forma a mostrar na tela os valores de todos os atributos"""

"""exercicio 24
    Baseando-se no exericio 23 adicione os métodos canalAcima e canalAbaixo, sendo que o método canalAcima deve
    sintonizar sempre o próximo canal em relação ao canal atual, onde ao chegar ao maior canal possível deverá voltar
    ao canal 1. O método canalAbaixo deve sintonizar sempre o canal anterior em relação ao canal atual, onde ao chegar
    ao canal 1 deverá voltar ao maior canal possível, simulando dessa forma o funcionamento de um televisor"""

"""exercicio 25
    Baseando-se no exercicio 24 adicione os métodos volumeAcima e volumeAbaixo, sendo que o métodos volumeAcima deve
    modificar o volume para o próximo nível de volume possível, onde ao chegar ao volume máximo não poderá possibiliar
    que o volume seja alterado. O método volumeAbaixo deve modificar o volume para o nível imediatamente inferior de
    volume em relação ao volume atual, não podemos ser menor do que zero, simulando dessa forma o funcionamento
    de um televisor"""


class Televisor:
    def __init__(self, numero_canais, volume_maximo, canal=1, volume=3, ligado=False):
        self.canal = canal
        self.numero_canais = numero_canais
        self.volume_maximo = volume_maximo
        self.volume = volume
        self.ligado = ligado

    def imprimir(self):
        print(f'O Televisor possui {self.numero_canais} canais e volume máximo de {self.volume_maximo}')
        if self.ligado:
            print(f'O Televisor encontra-se ligado no canal {self.canal}, com volume em {self.volume}.')
        else:
            print(f'O Televisor encontra-se desligado.')

    def ligar(self):
        if not self.ligado:
            self.ligado = True

    def desligar(self):
        if self.ligado:
            self.ligado = False
            self.volume = 3
            self.canal = 1

    def subir_canal(self):
        if self.canal < self.numero_canais:
            self.canal += 1
        elif self.canal == self.numero_canais:
            self.canal = 1

    def descer_canal(self):
        if self.canal > 1:
            self.canal -= 1
        elif self.canal == 1:
            self.canal = self.numero_canais

    def aumentar_volume(self):
        if self.volume < self.volume_maximo:
            self.volume += 1
        elif self.volume == self.volume_maximo:
            print('Volume Máximo já atingido.')

    def diminuir_volume(self):
        if self.volume > 0:
            self.volume -= 1
        elif self.volume == 0:
            print('Som mutado.')


# Codewars
tv = Televisor(13, 10)
tv.imprimir()
print()
tv.ligar()
for n in range(2):
    tv.subir_canal()
    tv.aumentar_volume()
tv.descer_canal()
tv.imprimir()
