import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-RAIZEN\SQLEXPRESS;"    
    "Database=AdventureWorks2017;"
)

conexao = pyodbc.connect(dados_conexao)
print('Conexão bem sucedida')


cursor = conexao.cursor()

comando = """SELECT * FROM Person.Person"""

cursor.execute(comando)
#cursor.commit() # só necessário se o comando acima edita o banco de dados. se é apenas leitura, não precisa do commit