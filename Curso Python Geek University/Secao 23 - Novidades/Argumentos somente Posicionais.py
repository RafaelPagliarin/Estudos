"""
Argumentos somente posicionais -> são argumentos que não permitem especialização de parametros
"""

# # Exemplo 1: sem especificar que o argumento seja somente posicional
# def cumprimenta_v1(nome):
#     return f'Olá {nome}'
#
# print(cumprimenta_v1('Rafael'))
# print(cumprimenta_v1(nome='Bárbara'))
#
#
# # Exemplo 2: especificando que o argumento seja posicional
# def cumprimenta_v2(nome, /):
#     return f'Olá {nome}'
#
# print(cumprimenta_v2('Rafael'))
# print(cumprimenta_v2(nome='Bárbara')) # Não funciona, pois o argumento é apenas posicional


# # Exemplo 3: Alguns argumentos apenas posicionais e outros não
# def cumprimentar_v3(nome, /, mensagem='Olá'):
#     return f'{mensagem} {nome}'
#
# print(cumprimentar_v3('Rafael'))
# print(cumprimentar_v3('Rafael', mensagem='Bom dia'))
# print(cumprimentar_v3('Bárbara', 'Seja bem vinda'))


# # Exemplo 4: Vários arguimentos apenas posicionais
#
# def cumprimentar_v4(nome, mensagem='Hello', /):
#     return f'{mensagem} {nome}'
#
# print(cumprimentar_v4('Rafael'))
# print(cumprimentar_v4('Bárbara', 'Seja bem vinda'))
# print(cumprimentar_v4('Rafael', mensagem='Bom dia'))

# # Exemplo 5: Ao contrário, quando informar o parametro é obrigatório -> tudo o que vem após o * é obrigatório nomear
#
# def cumprimentar_v5(*, nome):
#     return f'Olá {nome}'
#
# print(cumprimentar_v5(nome='Rafael'))
# print(cumprimentar_v5('Rafael')) #erro pois não informou o parametro

# #Exemplo 6: misturando as duas situações
#
# def cumprimentar_v6(nome, /, mensagem1='Olá', *, mensagem2):
#     return f'{mensagem1} {nome} {mensagem2}'
#
# print(cumprimentar_v6('Rafael', mensagem1='Hello', mensagem2='tenha um bom dia'))
# print(cumprimentar_v6('Bárbara', mensagem2='tenha um excelente dia'))
# print(cumprimentar_v6('Ivone', 'Olá', 'Vamos?'))