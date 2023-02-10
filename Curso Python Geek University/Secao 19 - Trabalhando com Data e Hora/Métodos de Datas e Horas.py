"""
Métodos de Data e Hora
================================================================================================================
# Diferença entre now() e today()

# now() podemos especificar um timezone (fuso horário)
agora = datetime.datetime.now()
print(agora)

hoje = datetime.datetime.today()
print(hoje)

================================================================================================================
#  Mudanças ocorrendo à meia noite - combine()

date = datetime.datetime # só para escrever menos

manutencao = date.combine((date.now() + datetime.timedelta(days=1)), datetime.time())

print(manutencao)
print(type(manutencao))
print(repr(manutencao))

================================================================================================================
# Encontrar o dia da semana - weekday()

# Os dias da semana no método weekday() começam no zero (0), sendo essa a segunda-feira
# 0 - Segunda-Feira (Monday)
# 1 - Terça-Feira (Tuesday)
# 2 - Quarta-Feira (Wednesday)
# 3 - Quinta-Feira (Thursday)
# 4 - Sexta-Feira (Friday)
# 5 - Sábado (Saturday)
# 6 - Domingo (Sunday)


date = datetime.datetime # só para escrever menos

manutencao = date.combine((date.now() + datetime.timedelta(days=1)), datetime.time())

print(manutencao.weekday())

================================================================================================================
#Calculando dia da semana de uma data específica

aniversario = input('Qual sua data de nascimento? dd/mm/yyyy: ')
aniversario = aniversario.split('/')
aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))

dia_da_semana = ('Segunda-Feira', 'Terça-Feira', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira', 'Sábado', 'Domingo')

for posicao, dia in enumerate(dia_da_semana):
    if posicao == aniversario.weekday():
        print(f'Você nasceu em um(a) {dia}')

================================================================================================================
# Formatando datas/horas com strftime() (String Format Time)

# dd/mm/yyyy hora:minuto

hoje = datetime.datetime.today()
print(hoje)

hoje_formatado = hoje.strftime('%d/%m/%Y')
# %Y = 4 digitos , %y = 2 digitos
# %m = mes numérico , %B = nome do mês (ingles), %b = iniciais do mês (ingles)
print(hoje_formatado)


# Formatando datas/horas com strptime() != strftime()

nascimento = datetime.datetime.strptime('10/04/1998', '%d/%m/%Y')
print(nascimento)

nascimento = input('Informe a data de nascimento: dd/mm/yyyy ')
nascimento = datetime.datetime.strptime(nascimento, '%d/%m/%Y')
print(nascimento)

================================================================================================================
# Formatando data para o mês aparecer em portugues


def formata_data(data):
    meses_pt = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
                'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

    for posicao, mes in enumerate(meses_pt):
        if posicao + 1 == data.month:
            return f'{data.day} de {mes} de {data.year}'


hoje = datetime.datetime.today()
hoje_formatado = formata_data(hoje)
print(hoje_formatado)

================================================================================================================
# Somente a hora

almoco = datetime.time(12, 30, 0)
print(almoco)

================================================================================================================
# Marcando tempo de execução do nosso código com timeit
import timeit

# Loop for
tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=100000)
print(tempo)
# List Comprehension
tempo = timeit.timeit('"-".join([str(n) for n in range(100)])', number=100000)
print(tempo)
# Map
tempo = timeit.timeit('"-".join(map(str, range(100)))', number=100000)
print(tempo)

================================================================================================================
import timeit, functools

def teste(n):
    soma = 0
    for num in range(n * 200):
        soma = soma + num ** num + 4
    return soma


print(timeit.timeit(functools.partial(teste, 2), number=10000))
"""



