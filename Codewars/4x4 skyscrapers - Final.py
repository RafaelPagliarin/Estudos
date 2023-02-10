def solve_puzzle (clues):
    from itertools import permutations

    ############################ variáveis ###########################################
    first_quarter = length = int(len(clues) * 1 / 4)
    second_quarter = int(len(clues) * 2 / 4)
    third_quarter = int(len(clues) * 3 / 4)
    forth_quarter = int(len(clues) * 4 / 4)
    letras = 'ABCDEFGHI'
    numeros = '123456789'
    quadrados = [a+b for a in letras[0:length] for b in numeros[0:length]]
    board = [quadrados[x:x + length] for x in range(0, len(quadrados), length)]
    possiveis = dict((q, [1+x for x in range(length)]) for q in quadrados)
    sum_values = 0

    ############################ 1ª parte ###########################################
    def criar_combinacoes_dicas():
        #maior dica possivel = length
        #tabela_dicas ((dica, dica_inversa, valor1, valor2, ..., valor(length))
        tabela_dicas = ()

        #criar uma permutation com todas as possiveis sequencias de andares
        andares = (v+1 for v in range(length))
        combinations = tuple(permutations(andares))
        dica = []
        dica_inversa = []

        for comb in combinations:
            cont = 1
            for x in range(1, len(comb)):
                higher = True
                for y in comb[0:x]:
                    if comb[x] < y:
                        higher = False
                if higher:
                    cont += 1
            dica.append(cont)

        for comb in combinations:
            comb = tuple(reversed(comb))
            cont2 = 1
            for x in range(1, len(comb)):
                higher = True
                for y in comb[0:x]:
                    if comb[x] < y:
                        higher = False
                if higher:
                    cont2 += 1
            dica_inversa.append(cont2)

        pack_combinacao = tuple(zip(dica, combinations, dica_inversa))
        return pack_combinacao

    def organizar_combinacoes():
        pack = criar_combinacoes_dicas()
        comb_list_aux = []
        for x in pack:
            list_aux = [x[0],[x[1]],x[2]]
            for y in pack:
                if x != y and x[0] == y[0] and x[2] == y[2]:
                    list_aux[1].append(y[1])
            comb_list_aux.append(list_aux[::])

        for x in comb_list_aux:
            outcomes_list = [set() for x in range(length)]
            for y in x[1]:
                for i in range(0, length):
                    outcomes_list[i].add(y[i])
            x[1] = outcomes_list[::]

        results = [i for n, i in enumerate(comb_list_aux) if i not in comb_list_aux[:n]]

        # adicionar combinações onde não existe dica_inversa (dica = 0)
        for i in range(1, length+1):
            zero_list = [i, [set('') for t in range(length)], 0]
            for k, x in enumerate(results):
                if x[0] == i:
                    for a, b in enumerate(x[1]):
                        zero_list[1][a] = zero_list[1][a] | b
            results.append(zero_list)
        return results

    ############################ 2ª parte ###########################################
    def usar_dicas(dica, dica_inversa, linha_atual):
        gabarito = organizar_combinacoes()
        for x in gabarito:
            if x[0] == dica and x[2] == dica_inversa:
                for i in range(0, length):
                    for j in range(1, length+1):
                        if j not in x[1][i] and j in possiveis[linha_atual[i]]:
                            possiveis[linha_atual[i]].remove(j)

    def verificar_dica_oposta(p):
        if 0 <= p < first_quarter:  # dicas da parte superior
            clue_inversa = clues[(third_quarter - 1) - p]
        elif first_quarter <= p < second_quarter:  # dicas do lado direito
            clue_inversa = clues[(forth_quarter - 1) + length - p]
        elif second_quarter <= p < third_quarter:  # dicas da parte inferior
            clue_inversa = clues[(third_quarter - 1) - p]
        elif third_quarter <= p <= forth_quarter:  # dicas do lado esquerdo
            clue_inversa = clues[(forth_quarter - 1) + length - p]
        return clue_inversa

    def buscar_interligados(quadrado, onlycol=False, onlyrow=False):
        l = quadrado[0]
        c = quadrado[1]
        linha_interligada = [x for x in quadrados if x[0] == l]
        coluna_interligada = [y for y in quadrados if y[1] == c]
        linha_interligada.remove(quadrado)
        coluna_interligada.remove(quadrado)
        interligados = linha_interligada + coluna_interligada
        if onlycol:
            return coluna_interligada
        if onlyrow:
            return linha_interligada
        return interligados

    def calcular_posicoes_dicas(p):
        if 0 <= p < first_quarter:  # dicas da parte superior
            quadrado_atual = board[0][p]
            quadrados_ligados = buscar_interligados(quadrado_atual, onlycol=True)
        elif first_quarter <= p < second_quarter:  # dicas do lado direito
            quadrado_atual = board[p - length][length-1]
            quadrados_ligados = buscar_interligados(quadrado_atual, onlyrow=True)
            quadrados_ligados = quadrados_ligados[::-1]
        elif second_quarter <= p < third_quarter:  # dicas da parte inferior
            quadrado_atual = board[length-1][(third_quarter - 1) - p]
            quadrados_ligados = buscar_interligados(quadrado_atual, onlycol=True)
            quadrados_ligados = quadrados_ligados[::-1]
        elif third_quarter <= p <= forth_quarter:  # dicas do lado esquerdo
            quadrado_atual = board[(forth_quarter - 1) - p][0]
            quadrados_ligados = buscar_interligados(quadrado_atual, onlyrow=True)
            quadrados_ligados = quadrados_ligados

        return quadrado_atual, quadrados_ligados

    ############################ 3ª parte ###########################################
    def checar_faltantes():
        for quadrado in quadrados:
            interligados_linha = buscar_interligados(quadrado, onlyrow=True)
            interligados_coluna = buscar_interligados(quadrado, onlycol=True)
            interligados_todos = buscar_interligados(quadrado)

            #caso 1: quadrado ainda não tem valor definido
            if len(possiveis[quadrado]) > 1:
                for i in range(1, length+1):
                    if all((i not in possiveis[x]) for x in interligados_linha):
                        possiveis[quadrado] = [i]
                        break
                    if all((i not in possiveis[y]) for y in interligados_coluna):
                        possiveis[quadrado] = [i]
                        break

                for w in interligados_todos:
                    if len(possiveis[w]) == 1 and possiveis[w][0] in possiveis[quadrado]:
                        possiveis[quadrado].remove(possiveis[w][0])

            # caso 2: quadrado tem valor definido
            elif len(possiveis[quadrado]) == 1:
                for x in interligados_linha:
                    if possiveis[quadrado][0] in possiveis[x]:
                        possiveis[x].remove(possiveis[quadrado][0])
                for y in interligados_coluna:
                    if possiveis[quadrado][0] in possiveis[y]:
                        possiveis[y].remove(possiveis[quadrado][0])

    def checar_regras_no_final():
        lista_restantes = []
        for k, v in possiveis.items():
            if len(v) > 1:
                lista_restantes.append(k)

        for i, h in enumerate(clues):
            if h != 0:
                dica = h
                primeiro, sequencia = calcular_posicoes_dicas(i)
                sequencia.insert(0, primeiro)

                if any(len(possiveis[x]) != 1 for x in sequencia):
                    lista_aux = []
                    lista_aux2 = []
                    lista_aux3 = []

                    for x in sequencia:
                        lista_aux.append(possiveis[x][::])

                    for x in range(len(lista_aux)):
                        if len(lista_aux[x]) > 1:
                            for j in lista_aux[x]:
                                if j not in lista_aux2[0:x]:
                                    lista_aux2.append(j)
                                    lista_aux[x].remove(j)
                        else:
                            lista_aux2.append(lista_aux[x][0])
                        lista_aux3.append(lista_aux[x][0])

                    cont = 1
                    for x in range(1, len(lista_aux2)):
                        higher = True
                        for y in lista_aux2[0:x]:
                            if lista_aux2[x] < y:
                                higher = False
                        if higher:
                            cont += 1

                    possivel2 = False
                    possivel3 = False
                    v2, v3, possivel_lista2, possivel_lista3 = 0,0,0,0

                    if cont == dica and dica != 1:
                        for k, v in enumerate(sequencia):
                            if v in lista_restantes:
                                teste_final = buscar_interligados(v)
                                if all((lista_aux2 != x for x in possiveis[y]) for y in teste_final):
                                    possivel_lista2 = [lista_aux2[k]]
                                    possivel2 = True
                                    v2 = v

                    cont = 1
                    for x in range(1, len(lista_aux3)):
                        higher = True
                        for y in lista_aux3[0:x]:
                            if lista_aux3[x] < y:
                                higher = False
                        if higher:
                            cont += 1

                    if cont == dica and dica != 1:
                        for k, v in enumerate(sequencia):
                            if v in lista_restantes:
                                teste_final = buscar_interligados(v)
                                if all((lista_aux3 != x for x in possiveis[y]) for y in teste_final):
                                    possivel_lista3 = [lista_aux3[k]]
                                    v3 = v
                                    possivel3 = True

                    if possivel2 and possivel3:
                        pass
                    if possivel2 and not possivel3:
                        possiveis[v2] = possivel_lista2
                    if not possivel2 and possivel3:
                        possiveis[v3] = possivel_lista3

        # loop para varrer os inputs (dicas)

    ############################ main code ###########################################
    for p, h in enumerate(clues):
        quadrado_atual, quadrados_ligados = calcular_posicoes_dicas(p)
        h_inversa = verificar_dica_oposta(p)
        quadrados_ligados.insert(0, quadrado_atual)
        usar_dicas(h, h_inversa, quadrados_ligados)

    while True:
        for x in possiveis.values():
            for i in x:
                sum_values += 1
        if sum_values == (len(clues)):
            list_answer = tuple(x[0] for x in possiveis.values())
            return tuple(list_answer[x:x + length] for x in range(0, len(list_answer), length))
        else:
            pass
            sum_values, teste, teste2 = 0,0,1
            while teste != teste2:
                teste = [i for i in possiveis.values()]
                checar_faltantes()
                teste2 = [i for i in possiveis.values()]

            checar_regras_no_final()

            teste, teste2 = 0, 1
            while teste != teste2:
                teste = [i for i in possiveis.values()]
                checar_faltantes()
                teste2 = [i for i in possiveis.values()]


# print(solve_puzzle(
# ( 2, 2, 1, 3,
#   2, 2, 3, 1,
#   1, 2, 2, 3,
#   3, 2, 1, 3 )))

print(solve_puzzle(( 0, 0, 1, 2,
              0, 2, 0, 0,
              0, 3, 0, 0,
              0, 1, 0, 0 )))

# solve_puzzle((3,2,2,3,2,1, 1,2,3,3,2,2, 5,1,2,2,4,3, 3,2,1,2,2,4))

# print(solve_puzzle(((1, 1, 4, 3), (3, 4, 1, 1), (4, 1, 3, 1), (1, 3, 1, 4))))
