from classes import *

c1 = Cliente('Rafael', 30)
c2 = Cliente('Bárbara', 29)
c3 = Cliente('Anita', 65)
c1.inserir_endereco('São José dos Campos', 'SP')
c2.inserir_endereco('Salvador', 'BA')
c2.inserir_endereco('Belo Horizonte', 'MG')
c3.inserir_endereco('Rio de Janeiro', 'RJ')

print(c1.nome)
c1.listar_enderecos()
#del c1
print()

print(c2.nome)
c2.listar_enderecos()
#del c2
print()

print(c3.nome)
c3.listar_enderecos()
#del c3
print()

print('#########################################################################')

