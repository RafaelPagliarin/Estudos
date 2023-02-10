# usar o pandas para manipulação de excel

# pandas trabalha com duas estruturas de dados:

# pseries - colunas de tabelas, parecido com uma lista
# diferença é que no pseries todos os elementos precisam ser do mesmo tipo

#dataframe - como se fosse uma planilha do excel, ou uma tabela de banco de dados.
# composto por colunas, linhas e índice.

import jupyterlab as jupyterlab
import pandas as pd

# 1. gerar arquivo excel (xlsx) a partir dos dados
'''
carros = {
    'marca': ['Fiat', 'Chevrolet', 'Ford', 'Fiat', 'Chevrolet'],
    'modelo': ['Marea', 'Chevette', 'Escort', 'Marea', 'Chevette'],
    'ano': ['1999', '1978', '1997', '1999', '1982']
}

# função para transformar o dict acima em um dataframe
dataframe = pd.DataFrame(carros) #o pandas gera a primeira coluna como contador de index

print(dataframe)

# transformar o dataframe acima em um xlsx, dar diretório e salvar
dataframe.to_excel('./carros.xlsx')
'''
# 2. importar arquivo xlsx e manipular os dados

# criando variavel e atribuindo uma tabela excel como dataframe pandas
dataframe = pd.read_excel('./carros.xlsx')

# ordenando dados do dataframe
# no exemplo, por ano dos carros
# sort_values('ano', ascending=False) -> segundo parametro é opcional, caso queria colocar na ordem decrescente.
'''
dataframe_ordenado = dataframe.sort_values('ano')

dataframe_ordenado.to_excel('./carros_ordenados.xlsx')
'''
# removendo registros duplicados
'''
dataframe = dataframe.drop_duplicates() #sem parametro = todas as colunas iguais para ser considerado duplicado

dataframe = dataframe.drop_duplicates('modelo') #com parametro = apenas as colunas ou linhas serão olhadas, deixando o 1º
'''

#
print(dataframe)

for i, row in dataframe.iterrows():
    print(f'{row.marca} - {row.modelo}- {row.ano}')

