"""
Trabalhando com deltas de data e hora

data_inicial
data_final

delta = data_final - data_inicial
"""

import datetime

#Calculando algo no passado
"""aniversario = datetime.datetime(1992, 3, 10)

hoje = datetime.datetime.now()

idade = aniversario - hoje

print(idade)"""


# Para frente no tempo
"""data_compra = datetime.datetime.now()
print(data_compra)

regra_boleto = datetime.timedelta(days=3)
print(regra_boleto)

vencimento_boleto = data_compra + regra_boleto
print(vencimento_boleto)"""
