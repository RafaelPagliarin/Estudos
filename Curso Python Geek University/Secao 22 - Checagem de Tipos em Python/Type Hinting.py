# definimos o tipo de dado que a função receberá e também podemos colocar o tipo de dado que será retornado

# ==========================================================================================================
# def cumprimentar(nome: str) -> str:
#     return f'Olá, {nome}'
#
#
# print(cumprimentar('Rafael'))
# ==========================================================================================================

# Pros e Contras
#
# Pros:
# - facilita encontrar erros (com mypy, por exemplo)
# - melhora documentação do seu código
# - melhora funcionalidade de IDES (te ajudando com sugestões e possiveis correções)
#
# Contras:
# - dificuldade em se acostumar, por não ser necessário desde o começo (só saiu no 3.5 e implementado no 3.7)
# - deixa um pouco mais lento os códigos (queda na performance)

# ==========================================================================================================

# # Sem type hinting
# def cabecalho(texto, alinhamento=True):
#     if alinhamento:
#         return f'{texto.title()}\n{"-" * len(texto)}'
#     else:
#         return f'{texto.title()}'.center(50, '#')
#
#
# print(cabecalho('Rafael Pagliarin'))
# print(cabecalho('Bárbara Trifler', alinhamento=False))
#
# ==========================================================================================================

# # Com type hinting
# def cabecalho(texto: str, alinhamento: bool = True) -> str:
#     if alinhamento:
#         return f'{texto.title()}\n{"-" * len(texto)}'
#     else:
#         return f'{texto.title()}'.center(50, '#')
#
#
# print(cabecalho('Rafael Pagliarin'))
# print(cabecalho('Bárbara Trifler', alinhamento=False))

# ====================================================================================================================

# # Annotations
#
# import math
#
#
# def circunferencia(raio: float) -> float:
#     return 2 * math.pi * raio
#
# # dá print nas annotations da função
# # print(circunferencia.__annotations__)
#
#
# nome: str = 'Rafael'
# peso: float = 104.3
# ativo: bool = True
#
# # dá print nas annotations das variáveis
# print(__annotations__)

# ===================================================================================


class Pessoa:
    def __init__(self, nome: str, idade: int, peso: float) -> None:
        self.__nome: str = nome
        self.__idade: int = idade
        self.__peso: float = peso

    def andar(self) -> str:
        return f'{self.__nome} está andando.'


p = Pessoa(nome='Rafael Pagliarin', idade=30, peso=104.3)

print(p.__dict__)

# a INSTANCIA não tem annotations, dá erro de atributo:
# print(p.__annotations__)

