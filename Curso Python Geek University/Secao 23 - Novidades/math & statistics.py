import math

# # math.prod -> retorna o produto de um container numérico
#
# nums_v1 = [2,3,6,8]
# nums_v2 = (2,3,6,8)
# nums_v3 = {2,3,6,8}
#
# print(math.prod(nums_v1))
# print(math.prod(nums_v2))
# print(math.prod(nums_v3))

#======================================================================================================================

# # math.isqrt -> retorna a parte inteira da raiz quadrada de um valor
#
# print(math.sqrt(9)) #3.0
# print(math.isqrt(9)) #3
#
# print(math.sqrt(17)) #4.123105625617661
# print(math.isqrt(17)) #4

#======================================================================================================================

# # math.dist -> retorna a distancia euclidiana entre dois pontos. 3D ou 2D
#
# #Pontos 3D
# p3d1 = (12, 50, 40)
# p3d2 = (6, 7, 13)
# #pontos 2D
# p2d1 = (12, 50)
# p2d2 = (6, 7)
#
# print(math.dist(p3d1, p3d2))
# print(math.dist(p2d1, p2d2))

#======================================================================================================================

# #math.hypot -> retorna a hipotenusa, ou norma euclidiana
# p3d1 = (12, 50, 40)
# p2d1 = (12, 50)
#
# print(math.hypot(*p3d1))
# print(math.hypot(*p2d1))

#======================================================================================================================

# Estatistica
import statistics

#======================================================================================================================

# # statistics.fmean -> calcula a media de numeros reais
#
# valores_reais = [1.45, 6.789, 3.45, 89.98765]
# valores_inteiros = [1, 6, 3, 89]
#
# print(statistics.fmean(valores_reais))
# print(statistics.fmean(valores_inteiros))
#
# # statistics.geometric_mean -> calcula a média geometrica de números reais
#
# print(statistics.geometric_mean(valores_reais))
# print(statistics.geometric_mean(valores_inteiros))
#======================================================================================================================

# statistics.multimode -> retorna o(s) valor(es) mais frequente em uma sequencia

seq1 = 'Geek University'
seq2 = [3, 5, 3, 7, 8, 9, 5, 3]
seq3 = [1,2,3,1,2,3,4,5,6]

print(statistics.multimode(seq1))
print(statistics.multimode(seq2))
print(statistics.multimode(seq3))

