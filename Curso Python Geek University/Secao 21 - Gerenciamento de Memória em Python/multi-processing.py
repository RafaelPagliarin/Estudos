from multiprocessing import Pool
import time

contador = 50000000


def contagem_regressiva(valor):
    while valor > 0:
        valor -= 1


if __name__ == '__main__':
    pool = Pool(processes=2)
    inicio = time.time()
    r1 = pool.apply_async(contagem_regressiva, [contador//4])
    r2 = pool.apply_async(contagem_regressiva, [contador//4])
    r3 = pool.apply_async(contagem_regressiva, [contador//4])
    r4 = pool.apply_async(contagem_regressiva, [contador//4])
    pool.close()
    pool.join()
    fim = time.time()

    print(f'Tempo em segundos: {fim - inicio}')
