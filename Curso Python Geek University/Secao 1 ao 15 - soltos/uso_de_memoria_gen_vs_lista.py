# utilizando lista
def fib_lista(max):
    lista = []
    a, b = 0, 1
    while len(lista) < max:
        lista.append(b)
        a, b = b, a + b
    return lista


# USANDO LISTA : RAM = 2450MB ~ 20% cpu
for n in fib_lista(100000):
    print(n)


# Usando generator
def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador += 1


# USANDO GERADORES : RAM = 1230MB ~ 11% cpu
for n in fib_gen(100000):
    print(n)

