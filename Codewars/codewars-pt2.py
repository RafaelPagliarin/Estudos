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

# import time
# def hamming(n):
#     count, number = 0, 1
#     while True:
#         teste = False
#         if number == 1 or number % 2 == 0 or number % 3 == 0 or number % 5 == 0:
#             for k in range(12):
#                 for j in range(12):
#                     for i in range(12):
#                         if number == 2 ** i * 3 ** j * 5 ** k:
#                             count += 1
#                             teste = True
#                             break
#                 if teste:
#                     break
#         if count == n:
#             return number
#         number +=1
#
#
# st = time.time()
# print(hamming(100))
# et = time.time()
# elapsed_time = (et - st) * 1000
#
# print('Execution time:', elapsed_time, 'miliseconds')

# =====================================================================================================================


# def square_digits(num):
#     return int(''.join(str(y) for y in [int(x)**2 for x in str(num)]))
#
#
# print(square_digits(9119))

# def open_or_senior(data):
#     answer = list()
#     for i in data:
#         if i[0] >= 55 and i[1] > 7:
#             answer.append('Senior')
#         else:
#             answer.append('Open')
#     return answer
#
#
# open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)])


# =====================================================================================================================

# def paperwork(n, m):
#     return 0 if n < 0 or m < 0 else n * m



# def alphabet_position(text):
#     alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
#     text = text.lower()
#     answer = ''
#     for letter in text:
#         for i, k in enumerate(alphabet):
#             if letter == k:
#                 answer += f'{i+1} '
#     print(answer)
#
#
# print(alphabet_position("The sunset sets at twelve o' clock."))


# def alphabet_position(text):
#     alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
#     return ''.join(f'{i + 1} ' for letter in text.lower() for i, k in enumerate(alphabet) if letter == k)
#
#
# print(alphabet_position("The sunset sets at twelve o' clock."))


# def count_positives_sum_negatives(arr):
#     answer = [0, 0]
#     if arr is None:
#         return None
#     for x in arr:
#         if x > 0:
#             answer[0] += 1
#         else:
#             answer[1] += x
#     return answer
#
#
# print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))

# def tribonacci(signature, n):
#     start = signature[::]
#     while len(start) < n:
#         start.append(sum(start[-3:]))
#     return start
#
# print(tribonacci([1, 1, 1], 10))

# from math import sqrt
# def find_next_square(sq):
#     if str(sqrt(sq))[-2:] != '.0':
#         return -1
#
#     while True:
#         sq += 1
#         if str(sqrt(sq))[-2:] == '.0':
#             return sq
#
#
# print(find_next_square(1))

# def high(x):
#     alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
#     listx = x.split()
#     list_score = []
#     for word in listx:
#         count = 0
#         for letter in word:
#             for k, v in enumerate(alphabet):
#                 if letter == v:
#                     count += k+1
#         list_score.append(count)
#
#     for k, n in enumerate(list_score):
#         if n == max(list_score):
#             return listx[k]
#
#
# print(high('take me to semynak'))

# def square_sum(numbers):
#     return sum(map(lambda x: x**2, numbers))

# def to_jaden_case(string):
#     return ' '.join(x.capitalize() for x in string.split())
#
#
# print(to_jaden_case("How can mirrors be real if our eyes aren't real"))

# def reverse_words(text):
#     return ' '.join(x[::-1] for x in text.split(' '))
#
#


# def is_square(n):
#     if str(n**0.5)[-2:] == '.0':
#         return True
#     return False
#
# print(is_square(4))


# def lovefunc( flower1, flower2 ):
#     if flower1 % 2 == 0 and flower2 % 2 == 0 or flower1 % 2 != 0 and flower2 % 2 != 0:
#         return False
#     return True
#
#
# def lovefunc( flower1, flower2 ):
#     return False if flower1 % 2 == 0 and flower2 % 2 == 0 or flower1 % 2 != 0 and flower2 % 2 != 0 else True

# def sum_two_smallest_numbers(numbers):
#     min1 = min(numbers)
#     numbers.remove(min(numbers))
#     min2 = min(numbers)
#     return min1 + min2
#
# def sum_two_smallest_numbers(numbers):
#     return sum(sorted(numbers)[:2])
#
#
#
# print(sum_two_smallest_numbers([5, 8, 12, 18, 22]))

# def find_smallest_int(arr):
#     return sorted(arr)[0]

# def find_smallest_int(arr):
#     return min(arr)

# def sort_array(source_array):
#     odds = [x for x in source_array if x%2!=0]
#     for x in range(len(source_array)):
#         if source_array[x] % 2 != 0:
#             source_array[x] = min(odds)
#             odds.remove(min(odds))
#     return source_array
#
#
# print(sort_array([5, 3, 2, 8, 1, 4]))

# from operator import itemgetter
# def top_3_words(text):
#     lower_acceptable = "a s d f g h j k l z x c v b n m q w e r t y u i o p ' ".split()
#     acceptable = lower_acceptable + [x.upper() for x in lower_acceptable]
#
#     for k, x in enumerate(text):
#         if x not in acceptable:
#             text = text.replace(x, ' ')
#         if x == "'" and not text[k-1].isalpha() and not text[k+1].isalpha():
#             text = text.replace(x, ' ')
#
#     text = text.split()
#
#     if len(text) == 0:
#         return []
#
#     nest = zip([text.count(x) for x in text], text)
#     nest = sorted(nest, key=itemgetter(0), reverse=True)
#     answer = []
#
#     while True:
#         for x in nest:
#             if x[1].lower() not in answer:
#                 answer.append(x[1].lower())
#             if len(answer) == 3:
#                 break
#         if x == nest[-1] or len(answer) == 3:
#             break
#     return answer
#
# # --------------------------------------------------------------------------------------
# from collections import Counter
# import re
#
#
# def top_3_words(text):
#     c = Counter(re.findall(r"[a-z']+", re.sub(r" '+ ", " ", text.lower())))
#     return [w for w,_ in c.most_common(3)]
#
# print(top_3_words("  '''  "))

