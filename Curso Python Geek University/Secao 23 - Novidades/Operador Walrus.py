# O Operador Walrus permite fazer a atribuição e retorno de valor em uma única expressão
# variavel := expressao

# nome = 'Geek University'
# print(nome)
#
# print(nome := 'Geek University')

# Modo "normal"
# cesta = []
# fruta = input('Informe a Fruta: ')
# while fruta != 'jaca':
#     cesta.append(fruta)
#     fruta = input('Informe a Fruta: ')

# Modo Walrus
cesta = []
while (fruta := input('Informe a Fruta: ')) != 'jaca':
    cesta.append(fruta)