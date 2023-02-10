"""
Utilizamos o mypy APENAS se estiver utilizando type hinting.

no terminal usamos:
mypy nome_arquivo.py

"""


def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f'{texto.title()}\n{"-" * len(texto)}'
    else:
        return f'{texto.title()}'.center(50, '#')


print(cabecalho('Rafael Pagliarin'))
print(cabecalho('Bárbara Trifler', alinhamento=False))
print(cabecalho('Ivone Tormim', alinhamento=True))


print(cabecalho.__annotations__)