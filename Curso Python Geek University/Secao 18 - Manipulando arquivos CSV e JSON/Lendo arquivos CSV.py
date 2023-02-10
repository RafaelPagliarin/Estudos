"""
Lendo arquivos CSV

CSV - Comma Separeted Values - Valores Separados por Vírgula

# Separador por vírgula:
1, 2, 3, 4, 5, 6
"geek" , "university" , "python" , "ciencia", "dados"

# Site de Dados fornecido pelo governo brasileiro
dados.gov.br/dataset

# Não ideal: (pois é trabalhoso)

with open('lutadores.csv', encoding='utf-8') as arquivo:
    dados = arquivo.read()
    #print(type(dados))
    print(dados)
    print('##################################################')
    dados = dados.split(',')[2::]
    print(dados)

A linguagem Python possui duas formas diferentes para ler dados em um arquivo CSV:
    - reader -> Permite que iteremos sobre as linhas do arquivo CSV como listas;
    - DictReader -> Permite que iteremos sobre as linhas do arquivo CSV como OrderedDicts;

    ps: por padrão ambos usam a vírgula como delimitador.
    para usar algum delimitador diferente, usamos o parâmetro "delimiter":
    leitor_csv = DictReader(arquivo, delimiter=',')

# Reader

from csv import reader

with open('lutadores.csv', encoding='utf-8') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv) # Pular o cabeçalho
    for linha in leitor_csv:
        # Cada linha é uma lista
        print(f'{linha[0]} nasceu no(a) {linha[1]} e mede {linha[2]} cm')

# DictReader

from csv import DictReader

with open('lutadores.csv', encoding='utf-8') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        print(f'{linha["Nome"]} nasceu no(a) {linha["País"]} e mede {linha["Altura (em cm)"]}')
"""

# DictReader

from csv import DictReader

with open('lutadores.csv', encoding='utf-8') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        print(f'{linha["Nome"]} nasceu no(a) {linha["País"]} e mede {linha["Altura (em cm)"]}')

