'''
Doctests
(o próprio teste funciona como doc para outros devs)

são testes que colocamos na docstrings das funções/métodos no Python

Para rodar um test de doctsts:

python -m doctest -v nome_do_modulo.py

def soma(a, b):
    """soma os números a e b

    >>> soma(1, 2)
    3
    """
    return a + b

'''



# Outro exemplo, aplicando TDD

def duplicar(valores):
    """duplica os valores de uma lista

    >>> duplicar([1,2,3,4])
    [2, 4, 6, 8]

    >>> duplicar([])
    []

    >>> duplicar(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    >>> duplicar([True, None])
    Traceback (most recent call last):
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return [2 * elemento for elemento in valores]
