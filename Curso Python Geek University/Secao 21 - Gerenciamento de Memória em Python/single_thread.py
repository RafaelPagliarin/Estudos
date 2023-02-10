import time
from threading import Thread

contador = 50000000


def contagem_regressiva(valor):
    while valor > 0:
        valor -= 1


inicio = time.time()
contagem_regressiva(contador)
fim = time.time()

print(f'Tempo em segundos: {fim - inicio}')

