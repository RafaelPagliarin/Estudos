# def last_digit(n1, n2):
#     if n2 == 0:
#         return 1
#     else:
#         return f'{pow(n1,n2,10)}'[-1]
#
#
# print(last_digit(3715290469715693021198967285016729344580685479654510946723, 68819615221552997273737174557165657483427362207517952651))

# ==========================================================================

from math import factorial
from functools import reduce


# def listPosition(word):
#     """Return the anagram list position of the word"""
#     if len(word) == 1:
#         return 1
#
#     unique_words = sorted(list(set(word)))
#     freq_letters = [word.count(letter) for letter in unique_words]
#     total_combinations = factorial(len(word)) / reduce(lambda x, y: x * y,
#                                                             [factorial(freq) for freq in freq_letters])
#
#     increment = [0] + [freq * total_combinations / len(word) for freq in freq_letters[:-1]]
#     increment = [sum(increment[:i + 1]) for i in range(len(increment))]
#
#     return int(increment[unique_words.index(word[0])] + listPosition(word[1:]))
#
#
#
# print(listPosition('IMMUNOELECTROPHORETICALLY'))

# =====================================================================================================================

# import time
#
# def fib(n):
#     fib_list = [0,1]
#
#     if 0 <= n <= 1:
#         return fib_list[n]
#
#     elif n > 1:
#         for x in range(n-1):
#             fib_list.append(fib_list[-1]+fib_list[-2])
#         return fib_list[-1]
#
#     elif n < 0:
#         nabs = abs(n)
#
#         for x in range(nabs-1):
#             fib_list.append((fib_list[-1] + fib_list[-2]))
#
#         if n % 2 == 0:
#             return fib_list[-1] * -1
#         else:
#             return fib_list[-1]
#
#
# st = time.time()
# fibn = fib(100000)
# et = time.time()
# elapsed_time = (et - st) * 1000
#
# print('Execution time:', elapsed_time, 'miliseconds')

# =====================================================================================================================
# from more_itertools import distinct_permutations as idp
# from itertools import permutations as pm
#
# def permutations(s):
#     answer = []
#     permu_sorted = sorted(set(pm(s)))
#     for value in permu_sorted:
#         aux = ''
#         for i in value:
#             aux += i
#         answer.append(aux)
#     return answer
#
# print(permutation('aabb'))


# def permutations(string):
#     return list("".join(p) for p in set(itertools.permutations(string)))

# =====================================================================================================================

# def solution(args):
#     answer = []
#     for value in args:
#         if
#
#     return answer
#
#
#
# print(solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))

# =====================================================================================================================

# def is_pangram(s):
#     alphabet = 'abcdefghijklmnopqrstuwxyz'
#     if all(letter in s.lower() for letter in alphabet):
#         return True
#     else:
#         return False
#
# print(is_pangram('The quick, brown fox jumps over the lazy dog!'))


# =====================================================================================================================

# def duplicate_encode(word):
#     new_word = ''
#     word = word.lower()
#     for letter in word:
#         if word.count(letter) == 1:
#             new_word += '('
#         else:
#             new_word += ')'
#     return new_word
#
#
# print(duplicate_encode('recede'))

# =====================================================================================================================

# def DNA_strand(dna):
#     dna_left, dna_right, answer = 'ATCG', 'TAGC', ''
#     for c in dna:
#         for k,v in enumerate(dna_left):
#             if c == v:
#                 answer += dna_right[k]
#     return answer
#
#
# print(DNA_strand('GTAT'))


# =====================================================================================================================

# def summation(num):
#     count = num
#     answer = 0
#     for c in range(count):
#         answer += num
#         num -= 1
#     return answer
#
#
# print(summation(22))

# =====================================================================================================================

# def abbrev_name(name):
#     name = name.upper().split()
#     return f'{name[0][0]}.{name[1][0]}'
#
# print(abbrev_name("Sam Harris"))

# =====================================================================================================================

# def solution(text, ending):
#     return text[-(len(ending)):] == ending
#
#
# print(solution("samurai", "ai"))

# =====================================================================================================================
