"""
Escrevendo em arquivos CSV

writer() -> cria um objeto que possibilita a escrita no arquivo CSV

writerow() -> Método para escrever cada linha, recebe uma lista.

#writer
from csv import writer

with open('filmes.csv', 'w') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Título', 'Gênero', 'Duração']) #Criação de cabeçalho
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informe a duração (em minutos): ')
            escritor_csv.writerow([filme, genero, duracao])

#DictWriter

from csv import DictWriter

with open('filmes2.csv', 'w') as arquivo:
    cabecalho = ['Titulo', 'Genero', 'Duração']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader() #escrever cabeçalho
    filme = None
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informe a duração (em minutos): ')
            escritor_csv.writerow({'Titulo': filme, 'Genero': genero, 'Duração': duracao}) #escrever linha
"""


