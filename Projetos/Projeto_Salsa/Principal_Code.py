"""
Need: Numa amostra (1000) de números aleatorios (de 6 digitos), determinar para cada numero a quantidade máxima de
 algarismos que se repetem.

Req 1: Gerar uma amostra de números aleatorios de 6 digitos
Req 2: Para cada número da amostra, encontrar o algarismo que mais se repete e guardar o valor
(ex, 268622 - algarismo que mais se repete "2" numero de repetições "3" vezes).
Req 3: gerar uma distribuição mostrando quantos numeros repetem 0 digitos, 1 digito, 2 digitos e assim por diante
"""

# Programa principal
from random import randint
from Funções import textos
amostra = list()
aux_amostra = dict()
while True:
    amostra.clear()
    textos.titulo('Amostra de \"N\" valores e distribuição de algarismos repetidos.', 1, 3)
    vz = int(input('Quantos valores deseja sortear? '))
    for i in range(0, vz):
        v = f'{str(randint(0, 999999)):0>6}'
        for r in range(0, 10):
            x = v.count((str(r)))
            if r == 0:
                max_rep = r
                vezes_rep = x
            else:
                if vezes_rep < x:
                    max_rep = r
                    vezes_rep = x
        aux_amostra['valor'] = v
        aux_amostra['algarismo'] = max_rep
        aux_amostra['repetições'] = vezes_rep
        amostra.append(aux_amostra.copy())
        aux_amostra.clear()
    textos.titulo(f'Dos valores gerados aleatoriamente, temos:', 1, 3)
    count = counttot = 0
    for i in range(1, 7):
        for p in amostra:
            if p['repetições'] == i:
                count += 1
        counttot += count
        print(f'{count:>4} com {i} algarismo(s) repetido(s).')
        count = 0
    print(f"{f'{counttot} números sorteados'}")
    while True:
        conti = str(input(f'\nDeseja visualizar detalhes? [S/N]: ')).strip().upper()
        if conti not in 'SN':
            print('Não entendi, digite novamente...')
        if conti == 'N':
            print('Ok!')
            break
        if conti == 'S':
            vis = int(input('Deseja visualizar os números com quantos algarismos repetidos? [1 até 6]: '))
            if vis not in range(1, 7):
                print('Valor invalido')
            else:
                print(f'\nValores sorteados com {vis} algarismos repetidos: ', end='')
                for p in amostra:
                    if p['repetições'] == vis:
                        print(p['valor'], end=' ')
                print()
    conti_ext = str(input('Deseja sortear outro valor? [S/N]: ')).strip().upper()
    if conti_ext not in 'SN':
        print('Opção inválida.')
    if conti_ext == 'N':
        print('Ok... encerrando programa, volte sempre!')
        break

