import time

# generator expression
gen_inicio = time.time()
print(sum(num for num in range(100000000))) # 100 milhões
gen_tempo = time.time() - gen_inicio

# list comprehension
list_inicio = time.time()
print(sum([num for num in range(100000000)])) # 100 milhões
list_tempo = time.time() - gen_inicio

print(f'Generator expression levou: {gen_tempo}')
print(f'List Comprehension levou: {list_tempo}')