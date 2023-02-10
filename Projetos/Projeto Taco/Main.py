import pandas as pd


tabela_taco = pd.read_excel('Tabela_Taco.xlsx')  # tabela onde as informações dos alimentos ficam armazenadas
tabela_cardapio = pd.read_excel('Cardapio.xlsx')  # tabela referencia para criação de cardapios
lista_pessoas = list()  # lista contendo dicionários com dados dos usuários e seus cardapios


def checar_continuidade():
    """Função responsável por checar se usuário deseja continuar realizando a ação presente"""
    checar = ' '
    while checar not in 'SN':
        checar = str(input('Deseja Continuar? [S/N] ')).strip().upper()[0]
        if checar not in 'SN':
            print('Não entendi...')
            continue
    if checar == 'S':
        return True
    else:
        return False


def calcular_idade(bday):
    """Função para calcular idade dos usuários"""
    from datetime import date
    today = date.today()
    checar_data = ((today.month, today.day) < (bday.month, bday.day))  # retorna 0 ou 1
    diferença = today.year - bday.year
    idade = diferença - checar_data
    return idade


# TABELA

def procurar_alimento(alimento):
    """Função que recebe nome do alimento, procura na tabela e caso encontre adiciona em nova tabela"""
    global tabela_taco
    tabela_alimento = pd.DataFrame()
    for name in tabela_taco['Descrição dos alimentos']:
        if alimento in str(name).lower():
            tabela_alimento = pd.concat(
                [tabela_alimento, tabela_taco.loc[tabela_taco['Descrição dos alimentos'] == name]])
    if tabela_alimento.shape[0] == 0:
        print('Nenhum alimento encontrado')
    return tabela_alimento


def adicionar_alimento():
    """Função responsável por adicionar alimento à tabela taco"""
    global tabela_cardapio
    global tabela_taco
    nome_alimento = input('Digite o nome do alimento: ')
    quantidade = float(input('Digite a porção, em gramas: '))
    proteina = float(input('Digite a quantidade de proteina, em gramas:'))
    gordura = float(input('Digite a quantidade de lipideos, em gramas:'))
    carboidrato = float(input('Digite a quantidade de carboidrato, em gramas:'))
    if quantidade == 100:
        energia = (proteina * 4) + (carboidrato * 4) + (gordura * 9)
    else:
        print('Irei atualizar a tabela do alimento digitado para o padrão de 100g')
        proteina = (proteina * quantidade) / 100
        carboidrato = (carboidrato * quantidade) / 100
        gordura = (gordura * quantidade) / 100
        energia = (proteina * 4) + (carboidrato * 4) + (gordura * 9)

    dict_alimento = {'Descrição dos alimentos': [nome_alimento],
                     'Energia (kcal)': energia,
                     'Proteína (g)': proteina,
                     'Lipídeos (g)': gordura,
                     'Carboidrato (g)': carboidrato
                     }
    add_alimento_DF = pd.DataFrame(dict_alimento)
    display(add_alimento_DF)
    check = ' '
    while check not in 'SN':
        check = str(input('Deseja adicionar esse elemento à tabela? [S/N]: ')).strip().upper()[0]
        if check not in 'SN':
            print('Não entendi...')
    if check == 'S':
        print('Adicionando alimento...')
        tabela_taco = pd.concat([tabela_taco, add_alimento_DF], ignore_index=True)
        display(tabela_taco)
    else:
        print('Alimento não adicionado.')


def remover_alimento_taco(alimento):
    """Função responsável por remover alimento da tabela taco"""
    global tabela_cardapio
    global tabela_taco
    tabela_alimento = pd.DataFrame()
    tabela_alimento = procurar_alimento(alimento)
    if tabela_alimento.shape[0] == 0:
        return
    else:
        display(tabela_alimento)
        remover = int(input('Deseja o número do indice do alimento que deseja remover: '))
        tabela_taco = tabela_taco.drop(remover, axis=0)
        print('Item removido com sucesso')
        display(tabela_taco)


# CARDAPIOS

def puxar_alimento(alimento, pessoa):
    """Função responsável por pegar um alimento da tabela taco e adicionar à
    tabela cardapio do usuário selecionado"""
    global tabela_cardapio
    global lista_pessoas
    tabela_alimento = pd.DataFrame()
    # procurando alimento e mostrando na tela
    tabela_alimento = procurar_alimento(alimento)
    print('Foram encontrados estes alimentos: ')
    display(tabela_alimento)
    # selecionando o indice do alimento
    index = int(input('Número do alimento desejado: '))
    # adicionando valores de quantidade e nome da refeição
    tabela_alimento.at[index, 'Quantidade'] = int(input('Quantas gramas ou unidades do alimento deseja adicionar? '))
    # alterações caso porção não seja padrão
    if tabela_alimento.at[index, 'Quantidade'] != 100 or tabela_alimento.at[index, 'Quantidade'] != 1:
        tabela_alimento.at[index, 'Proteína (g)'] = ((
                tabela_alimento.at[index, 'Quantidade'] * tabela_alimento.at[index, 'Proteína (g)'])) / 100
        tabela_alimento.at[index, 'Lipídeos (g)'] = ((
                tabela_alimento.at[index, 'Quantidade'] * tabela_alimento.at[index, 'Lipídeos (g)'])) / 100
        tabela_alimento.at[index, 'Carboidrato (g)'] = ((
                tabela_alimento.at[index, 'Quantidade'] * tabela_alimento.at[index, 'Carboidrato (g)'])) / 100
        tabela_alimento.at[index, 'Fibra Alimentar (g)'] = ((
                tabela_alimento.at[index, 'Quantidade'] * tabela_alimento.at[index, 'Fibra Alimentar (g)'])) / 100
        tabela_alimento.at[index, 'Energia (kcal)'] = ((tabela_alimento.at[index, 'Proteína (g)'] * 4) +
                                                       (tabela_alimento.at[index, 'Lipídeos (g)'] * 9) +
                                                       (tabela_alimento.at[index, 'Carboidrato (g)'] * 4))
    tabela_alimento.at[index, 'Refeição'] = str(
        input('A qual refeição deseja adicionar esse alimento? ')).strip().title()
    # adicionando o alimento selecionado à tabela cardapio
    lista_pessoas[pessoa]['Tabela_Cardapio'] = pd.concat(
        [lista_pessoas[pessoa]['Tabela_Cardapio'], tabela_alimento.loc[[index]]], ignore_index=True, axis=0)
    display(lista_pessoas[pessoa]['Tabela_Cardapio'])


def dividir_cardapio(pessoa):
    """Função responsável por dividir o cardapio do usuario selecionado para facilitar a visualização"""
    global lista_pessoas
    cardapio_separado = lista_pessoas[pessoa]['Tabela_Cardapio']
    cardapio_separado = cardapio_separado[
        ['Energia (kcal)', 'Proteína (g)', 'Lipídeos (g)', 'Carboidrato (g)', 'Fibra Alimentar (g)',
         'Refeição']].groupby(['Refeição']).sum()
    cardapio_separado = cardapio_separado.round(1)
    display(cardapio_separado)


def remover_alimento_cardapio(pessoa):
    """Função responsável por remover algum alimento do cardapio do usuário selecionado"""
    global lista_pessoas
    display(lista_pessoas[pessoa]['Tabela_Cardapio'])
    remover = int(input('Deseja o número do indice do alimento que deseja remover: '))
    lista_pessoas[pessoa]['Tabela_Cardapio'] = lista_pessoas[pessoa]['Tabela_Cardapio'].drop(remover, axis=0)
    print('Item removido com sucesso')
    display(tabela_cardapio)


# USUÁRIOS


def colher_informações():
    """Função responsável por colher as informações de um novo usuário e criar um dicionário com elas,
    retornando tal dicionário"""
    from datetime import date
    usuario = dict()
    sexo = ' '

    FA = 0
    usuario['Nome'] = str(input('Nome Completo: ')).strip().title()
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if sexo not in 'MF':
            print('Informação inválida, por favor responda novamente')
    usuario['Sexo'] = sexo
    usuario['Peso'] = float(input('Peso, em kg: '))
    usuario['Altura'] = float(input('Altura, em cm: '))
    print('data de nascimento: ')
    dia_bday = int(input('dia: '))
    mes_bday = int(input('mês: '))
    ano_bday = int(input('ano: '))
    usuario['Data_Nascimento'] = date(ano_bday, mes_bday, dia_bday)
    usuario['Idade'] = calcular_idade(usuario['Data_Nascimento'])
    while FA not in range(1, 5):
        print('''         Fator de Atividade (FA):
        [1] sedentário
        [2] levemente ativo
        [3] treino e cardio iniciante a intermediário quase todos os dias com rotina de pouca atividade
        [4] treino e cardio avançado ou extremamente avançado com rotina de pouca atividade
        [5] treino e cardio avançado ou extremamente avançado com rotina de muita atividade ou hormonizado
        ''')
        FA = float(input('Fator de Atividade: '))
        if FA == 1:
            usuario['Fator_Atividade'] = 1.3
        elif FA == 2:
            usuario['Fator_Atividade'] = 1.4
        elif FA == 3:
            usuario['Fator_Atividade'] = 1.5
        elif FA == 4:
            usuario['Fator_Atividade'] = 1.6
        elif FA == 5:
            usuario['Fator_Atividade'] = 1.7
        else:
            print('Opção inválida')
            continue
    if sexo == 'F':
        usuario[
            'GCD'] = f'{(usuario["Fator_Atividade"] * (655.09 + (9.563 * usuario["Peso"]) + (1.85 * usuario["Altura"]) - (4.676 * usuario["Idade"]))):.2f}'
    elif sexo == 'M':
        usuario[
            'GCD'] = f'{(usuario["Fator_Atividade"] * (66.47 + (13.75 * usuario["Peso"]) + (5.0 * usuario["Altura"]) - (6.8 * usuario["Idade"]))):.2f}'

    usuario['Tabela_Cardapio'] = pd.DataFrame()
    usuario['Tabela_Cardapio'] = pd.concat([usuario['Tabela_Cardapio'], tabela_cardapio], ignore_index=True)

    return usuario


def visualizar_usuários():
    """Função responsável por mostrar uma lista com todos os usuários cadastrados"""
    global lista_pessoas
    if len(lista_pessoas) != 0:
        pessoas_DF = pd.DataFrame(lista_pessoas)
        display(pessoas_DF[['Nome', 'Peso', 'Altura', 'Idade', 'GCD']])
    else:
        print('Nenhum usuário cadastrado.')


def detalhar_usuário():
    """Função responsável por mostrar melhor os dados do usuário selecionado"""
    global lista_pessoas
    visualizar_usuários()
    escolha = int(input('Digite o código do usuário: '))
    pessoas_DF = pd.DataFrame(lista_pessoas)
    print(pessoas_DF.loc[escolha])


def atualizar_usuário():
    """Função responsável por atualizar o usuário selecionado"""
    global lista_pessoas
    from datetime import date
    FA = 0
    visualizar_usuários()
    cod_usuario = int(input('Digite o código do usuário: '))
    print(f'Editando {lista_pessoas[cod_usuario]["nome"]}')
    lista_pessoas[cod_usuario]['Idade'] = calcular_idade(lista_pessoas[cod_usuario]['Data_Nascimento'])
    lista_pessoas[cod_usuario]['Peso'] = float(input('Peso, em kg: '))
    lista_pessoas[cod_usuario]['Altura'] = float(input('Altura, em cm: '))
    while FA not in range(1, 5):
        print('''         Fator de Atividade (FA):
        [1] sedentário
        [2] levemente ativo
        [3] treino e cardio iniciante a intermediário quase todos os dias com rotina de pouca atividade
        [4] treino e cardio avançado ou extremamente avançado com rotina de pouca atividade
        [5] treino e cardio avançado ou extremamente avançado com rotina de muita atividade ou hormonizado
        ''')
        FA = float(input('Fator de Atividade: '))
        if FA == 1:
            lista_pessoas[cod_usuario]['Fator_Atividade'] = 1.3
        elif FA == 2:
            lista_pessoas[cod_usuario]['Fator_Atividade'] = 1.4
        elif FA == 3:
            lista_pessoas[cod_usuario]['Fator_Atividade'] = 1.5
        elif FA == 4:
            lista_pessoas[cod_usuario]['Fator_Atividade'] = 1.6
        elif FA == 5:
            lista_pessoas[cod_usuario]['Fator_Atividade'] = 1.7
        else:
            print('Opção inválida')
            continue

    if lista_pessoas[cod_usuario]['sexo'] == 'F':
        lista_pessoas[cod_usuario][
            'GCD'] = f'{(lista_pessoas[cod_usuario]["Fator_Atividade"] * (655.09 + (9.563 * lista_pessoas[cod_usuario]["Peso"]) + (1.85 * lista_pessoas[cod_usuario]["Altura"]) - (4.676 * lista_pessoas[cod_usuario]["Idade"]))):.2f}'
    elif lista_pessoas[cod_usuario]['sexo'] == 'M':
        lista_pessoas[cod_usuario][
            'GCD'] = f'{(lista_pessoas[cod_usuario]["Fator_Atividade"] * (66.47 + (13.75 * lista_pessoas[cod_usuario]["Peso"]) + (5.0 * lista_pessoas[cod_usuario]["Altura"]) - (6.8 * lista_pessoas[cod_usuario]["Idade"]))):.2f}'


def remover_usuário():
    """Função responsável por remover o usuário selecionado"""
    global lista_pessoas
    visualizar_usuários()
    escolha = int(input('Digite o código do usuário: '))
    lista_pessoas.pop(escolha)


# Menu

def menu_primario():
    print()
    texto = 'Projeto Taco - v1.0'
    print('~' * (len(texto) + 4))
    print(f'  {texto}')
    print('~' * (len(texto) + 4))
    print('''
    [1] Alimentos
    [2] Cardapios
    [3] Usuários
    [4] Salvar
    [5] Encerrar Programa
    ''')
    opção = int(input('Digite a opção desejada: '))
    if opção not in range(1, 5):
        print('opção inválida')
    else:
        return opção


def menu_alimentos():
    print()
    texto = 'Menu: Alimentos'
    print('~' * (len(texto) + 4))
    print(f'  {texto}')
    print('~' * (len(texto) + 4))
    print('''
    [1] Pesquisar Alimento
    [2] Adicionar Alimento
    [3] Remover Alimento
    [4] Voltar
    ''')
    opção = int(input('Digite a opção desejada: '))
    if opção not in range(1, 5):
        print('opção inválida')
    else:
        return opção


def menu_cardápio():
    global lista_pessoas
    global pessoa

    print()
    texto = f'Cardápio de {lista_pessoas[pessoa]["Nome"]}'
    print('~' * (len(texto) + 4))
    print(f'  {texto}')
    print('~' * (len(texto) + 4))
    print('''
    [1] Visualizar Cardápio
    [2] Adicionar Alimento ao Cardápio
    [3] Remover Alimento do Cardápio
    [4] Voltar
    ''')
    opção = int(input('Digite a opção desejada: '))
    if opção not in range(1, 5):
        print('opção inválida')
    else:
        return opção


def menu_usuário():
    print()
    texto = 'Menu: Usuários'
    print('~' * (len(texto) + 4))
    print(f'  {texto}')
    print('~' * (len(texto) + 4))
    print()
    visualizar_usuários()
    print()
    print('''
    [1] Visualizar Detalhes de Usuário
    [2] Adicionar Novo Usuário
    [3] Atualizar Usuário
    [4] Remover Usuário
    [5] Voltar
    ''')
    opção = int(input('Digite a opção desejada: '))
    if opção not in range(1, 6):
        print('opção inválida')
    else:
        return opção


while True:
    continuar = True
    escolha = menu_primario()  # menu principal - escolher uma entre 4 opções
    if escolha == 1:  # menu alimentos
        while True:
            escolha_2 = menu_alimentos()
            if escolha_2 == 1:  # pesquisar alimento
                while continuar:
                    print(procurar_alimento(str(input('Deseja procurar qual alimento: ')).strip().lower()))
                    continuar = checar_continuidade()
            elif escolha_2 == 2:  # adicionar alimento
                while continuar:
                    adicionar_alimento()
                    continuar = checar_continuidade()
            elif escolha_2 == 3:  # voltar
                while continuar:
                    remover_alimento_taco(str(input('Deseja procurar qual alimento: ')).strip().lower())
                    continuar = checar_continuidade()
            else:
                break
    elif escolha == 2:  # menu cardapio
        while True:
            visualizar_usuários()
            pessoa = int(input('Cardapio de qual usuário deseja visualizar? '))
            escolha_2 = menu_cardápio()
            if escolha_2 == 1:  # visualizar cardapio
                display(lista_pessoas[pessoa]['Tabela_Cardapio'])
                dividir_cardapio(pessoa)
            elif escolha_2 == 2:  # adicionar alimento ao cardapio
                while continuar:
                    puxar_alimento(str(input('Deseja procurar qual alimento: ')).strip().lower(), pessoa)
                    continuar = checar_continuidade()
            elif escolha_2 == 3:
                remover_alimento_cardapio(pessoa)
            else:
                break
    elif escolha == 3:  # menu usuário
        while True:
            escolha_2 = menu_usuário()  # menu usuario
            if escolha_2 == 1:  # visualizar detalhes de usuário
                if len(lista_pessoas) == 0:
                    continue
                else:
                    detalhar_usuário()
            elif escolha_2 == 2:  # adicionar novo usuário
                lista_pessoas.append(colher_informações())
            elif escolha_2 == 3:  # atualizar usuário existente
                atualizar_usuário()
            elif escolha_2 == 4:  # remover usuário
                remover_usuário()
            elif escolha_2 == 5:  # voltar
                break
    elif escolha == 4:  # salvar arquivos
        for v, k in enumerate(lista_pessoas):
            k['Tabela_Cardapio'].to_excel(f"{k['Nome']}.xlsx")
    elif escolha == 5:  # encerrar programa
        print('\n Encerrando programa')
        break
    else:
        print('Opção inválida')
        continue
