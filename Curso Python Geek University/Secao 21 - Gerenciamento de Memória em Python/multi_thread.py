import time
from threading import Thread

contador = 50000000


def contagem_regressiva(valor):
    while valor > 0:
        valor -= 1


t1 = Thread(target=contagem_regressiva, args=(contador//2,))
t2 = Thread(target=contagem_regressiva, args=(contador//2,))

inicio = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
fim = time.time()

print(f'Tempo em segundos: {fim - inicio}')