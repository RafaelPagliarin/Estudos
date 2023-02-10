"""
Associação - USA   outro objeto
Agregação - TEM   outro objeto
Composição - DONO  de outro objeto
Herança - É  outro objeto
"""

from classes import *

p1 = Pessoa('Rafael', 30)
print(p1.nome)
p1.falar()
#p1.comprar()
#p1.estudar()
print()

c1 = Cliente('Babi', 29)
print(c1.nome)
c1.falar()
c1.comprar()
#c1.estudar()
print()

a1 = Aluno('Xuxa', 64)
print(a1.nome)
a1.falar()
#a1.comprar()
a1.estudar()