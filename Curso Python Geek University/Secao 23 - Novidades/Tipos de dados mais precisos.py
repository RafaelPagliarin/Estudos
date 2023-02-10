"""
int, str, float, List, Set, Dict, etc

"""

# def dobro(valor: int) -> int:
#     return valor * 2
#
# print(dobro(8))

"""
- Literal
- Union
- Final
- Typed dictionaries
- Protocols

ps: esses tipos só são uteis quando usados junto com mypy para checar as tipagems. No python em si, não ocorrerá erros.
"""


##### Literal type

from typing import Literal

# def pegar_status(usuario: str) -> Literal['conectado', 'desconectado']:
#     pass

# def calcula_v1(operacao: str, num1: int, num2: int) -> None:
#     if operacao == '+':
#         print(f'{num1} + {num2} = {num1 + num2}')
#     elif operacao == '-':
#         print(f'{num1} - {num2} = {num1 - num2}')
#     else:
#         raise ValueError(f'Operação inválida {operacao!r}') # !r no final colocou em aspas simples a variavel

# def calcula_v2(operacao: Literal['+', '-'], num1: int, num2: int) -> None:
#     if operacao == '+':
#         print(f'{num1} + {num2} = {num1 + num2}')
#     elif operacao == '-':
#         print(f'{num1} - {num2} = {num1 - num2}')
#     else:
#         raise ValueError(f'Operação inválida {operacao!r}') # !r no final colocou em aspas simples a variavel
#
# calcula_v2('+', 6, 4)
# calcula_v2('-', 10, 2)
# calcula_v2('*', 3, 5)


##### Union
# from typing import Union
#
# def soma(num1: int, num2: int) -> Union[str, int]:
#     resultado: int = num1 + num2
#
#     if resultado > 50:
#         return f'O valor {resultado} é muito grande.'
#     else:
#         return resultado
#

# ##### Final
# from typing import Final
#
# NOME: Final = 'Geek'
# print(NOME)
#
# NOME = 'University'
# print(NOME)
#
# from typing import final
#
# @final
# class Pessoa:
#     pass
#
# class Estudante(Pessoa):
#     pass
#
#     @final
#     def estudar(self):
#         print('Estou estudando')
#
#
# class Estagiario(Estudante):
#     pass
#
#     def estudar(self):
#         print('Estudando e trabalhando')


##### Typed Dictionaries

# from typing import TypedDict
#
# class CursoPython(TypedDict):
#     versao: str
#     atualizacao: int
#
# geek = CursoPython(versao='3.11', atualizacao=2023)
#
# print(geek)


##### Protocols - Não entendi Matrix 
from typing import Protocol

class Curso(Protocol):
    titulo: str

def estudar(valor: Curso) -> None:
    print(f'Estou estudando o curso {valor.titulo}')

class Venda:
    pass

v1 = Venda()
estudar(v1)

