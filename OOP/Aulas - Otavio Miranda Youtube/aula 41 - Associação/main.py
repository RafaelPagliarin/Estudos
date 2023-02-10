from classes import *

escritor = Escritor('Joãozinho')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

escritor.ferramenta = maquina
escritor.ferramenta.escrever()

escritor.ferramenta = caneta
escritor.ferramenta.escrever()