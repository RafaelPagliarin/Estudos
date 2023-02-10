"""
Assertions (Afirmações/Checagens/Questionamentos)

palavra reservada: assert

usamos assert em uma expressão que queremos checar se é válida ou não.
Se a expressão for verdadeira, o assert returna None, caso seja falsa levanta um erro do tipo AssertionError

OBS: Podemos especificar, opcionalmente, um segundo argumento ou mesmo uma mensagem de erro personalizada

OBS: A palavra assert pode ser utilizada em qualquer função ou código... não precisa ser exclusivamente nos testes
------------------------------------------------------------------------------------------------------------------------

def somar_numeros_positivos(a, b):
    assert a > 0 and b > 0, 'Ambos números precisam ser positivos'
    return a + b

ret = somar_numeros_positivos(-2, 4) #assertionerror
ret = somar_numeros_positivos(2, 4) #6
print(ret)

# ALERTA : CUIDADO AO UTILIZAR 'assert'

Se o programa Python for executado com o parâmetro -O (letra o, não número zero), nenhum assertion será validado
Ou seja, todas as suas validações já eram.


"""


def somar_numeros_positivos(a, b):
    assert a > 0 and b > 0, 'Ambos números precisam ser positivos'
    return a + b


#ret = somar_numeros_positivos(-2, 4) #assertionerror
ret = somar_numeros_positivos(2, 4) #6
print(ret)


def comer_fast_food(comida):
    assert comida in [
        'pizza',
        'sorvete',
        'doces',
        'batata frita',
        'cachorro quente'
    ], 'A comida precisa ser fast food'
    return f'Eu estou comendo {comida}'


comida = input('Informe a comida: ')
print(comer_fast_food(comida))

