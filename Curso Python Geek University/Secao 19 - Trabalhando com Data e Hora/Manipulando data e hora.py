"""
Manipulando Data e Hora

Python possui módulo built-in para se trabalhar com data e hora chamado datetime

"""

import datetime

#print(dir(datetime))
#print(datetime.datetime.now()) #2022-11-21 14:50:03.040977


# replace() -> para fazer reajustes na data/hora
#year, month, day, hour, minute, second, microsecond
"""inicio = datetime.datetime.now()
print(inicio)
inicio = inicio.replace(year=2023)
print(inicio)"""

"""evento = datetime.datetime(2022, 1, 1, 0)
print(evento)"""

# Recebendo dados do usuário e convertendo para data
"""nascimento = input('informe sua data de nascimento (dd/mm/yyyy): ')
nascimento = nascimento.split('/')
nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))
print(nascimento)"""

# Acessando os elementos de data e hora individualmente
"""evento = datetime.datetime.now()

print(evento.year)
print(evento.month)
print(evento.day)
print(evento.hour)
print(evento.minute)
print(evento.second)
print(evento.microsecond)"""

# Pegando apenas 1 elemento de uma vez.
print(datetime.datetime.now().year)
