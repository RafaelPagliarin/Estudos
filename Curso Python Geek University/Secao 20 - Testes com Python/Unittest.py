"""
Introdução ao módulo Unittest

Unitest -> Codewars Unitários

Teste unitário é a forma de se testar unidades individuais de código fonte.

unidades individuais podem ser: funções, métodos, classes, módulos, etc.

#OBS: teste unitário não é algo específico da linguagem Python. É algo referente a programação em si.

Para criar nossos testes, criamos classes que herdam de unitttest.TestCase
e a partir de então ganhamos todos os 'assertions' presentes no módulo.

Para rodar os testes, utilizamos unittest.main()

TestCase -> casos de teste para sua unidade


# Para ver quais métodos de asserts são usados
https://docs.python.org/3/library/unittest.html


por convenção todos os testes em um test case devem ter seu nome iniciado com test_

1. Para executar os testse com unittest:
pythyon nome_do_modulo.py

2. Para executar os testes com unittest no modo verbose
python nome_do_modulo.py -v

# Docstrings nos testes

Podemos acrescentar (e é recomendado) adicionar docstrings nos testes, e eles aparecerão nos testes com modo verbose
"""
