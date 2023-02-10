import random

NAIPES = '♢ ♤ ♡ ♧'.split()
CARTAS = '4 5 6 7 Q J K A 2 3'.split()


def embaralhar_baralho():
    """Embaralha um baralho de truco"""
    baralho = [(c, n) for c in CARTAS for n in NAIPES]
    random.shuffle(baralho)
    return baralho


def distribuir_cartas(baralho):
    """Gerencia a mão de cartas de acordo com o deck embaralhado"""
    mao = []
    for x in range(4):
        mao.append([v for v in baralho[:3]])
        [baralho.pop(0) for x in range(3)]
    vira = baralho[0]
    baralho.pop(0)
    return mao, vira


def jogar():
    """Inicia um jogo de cartas para 4 jogadores"""
    cartas = embaralhar_baralho()
    jogadores = 'P1 P2 P3 P4'.split()
    n = distribuir_cartas(cartas)
    maos = {j: m for j, m in zip(jogadores, n[0])}

    for jogador, cartas in maos.items():
        carta = ' '.join(f'{j}{c}' for (j, c) in cartas)
        print(f'{jogador}: {carta}')
    print(f"Vira: {n[1][0]}{n[1][1]}")


if __name__ == '__main__':
    jogar()

