import math

# Type hinting aprendido, 'padrão'
# def circunferencia(raio: float) -> float:
#     return 2 * math.pi * raio


# Type hinting com comentários:
def circunferencia(raio):
    # type: (float) -> float
    return 2 * math.pi * raio


print(circunferencia(2))


# Tipo 1
def cabecalho(texto, alinhamento=True):
    # type: (str, bool) -> str
    if alinhamento:
        return 'a'
    else:
        return 'b'


cabecalho(texto='teste', alinhamento=False)


# Tipo 2
def cabecalho2(
        texto,  # type: str
        alinhamento=True  # type: bool
):  # type: (...) -> str
    if alinhamento:
        return 'a'
    else:
        return 'b'
    

print(cabecalho(texto='Codewars', alinhamento=True))