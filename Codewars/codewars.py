# def end_corona(recovers, new_cases, active_cases):
#
#     while x != 0:
#         0 == active_cases + new_cases * x - recovers * x
#         0 == active_cases + x * (new_cases - recovers)
#         return round((-1 * active_cases)/(new_cases - recovers))
#
#
#
# end_corona(4000, 2000, 77000)

# ==========================================================================

# def dna_to_rna(dna):
#     rna = ' '
#     for letter in dna:
#         if letter == 'A':
#             rna += 'U'
#         elif letter == 'T':
#             rna += 'A'
#         elif letter == 'G':
#             rna += 'C'
#         elif letter == 'C':
#             rna += 'G'
#     return rna


# def order(sentence):
#     new_sentence = ''
#     for number in range(10):
#         for word in sentence.split():
#             if str(number) in word:
#                 new_sentence = new_sentence + ' ' + word
#     return new_sentence.strip()

# def order(words):
#   return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))
# test.isnumeric()
#
#
# print(order("is2 Thi1s T4est 3a"))


"""def find_short(s):
    num = 1
    while True:
        for word in s.split():
            if len(word) == num:
                return num
        num += 1
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def find_short(s):
    return min(len(x) for x in s.split())

print(find_short("bitcoin take over the world maybe who knows perhaps"))"""


"""def solution(number):
    sum = 0
    if number == 0:
        return 0
    for n in range(number-1, -1, -1):
        print(n)
        if n % 3 == 0 or n % 5 == 0:
            sum += n
    return sum

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)


print(solution(6))"""


"""def high_and_low(numbers):
    return f'{max(numbers.split(), key=int)}, {min(numbers.split(), key=int)}'"""

#
# def friend(x):
#     return filter(lambda x: x if len(x) == 4,)


#print(friend())


#print(list(filter(lambda x: ''.join(x) if len(x) == 4 else None, ["Ryan", "Kieran" , "Mark"])))


# def persistence(n):
#     persis = 0
#     n = list((int(a) for a in str(n)))
#     while len(n) > 1:
#         r = 1
#         for digit in n:
#             r *= digit
#         persis += 1
#         n = list((int(a) for a in str(r)))
#     return persis
#
# print(persistence(39))


# def solution(s):
#     s = list(s)
#     for position, letter in enumerate(s):
#         if letter.isupper():
#             s.insert(position-1, ' ')
#     return s
#
#
#
# print(solution("camelCasing"))

# s= "camelCasing"
#
# new_string = ""
# for i in s:
#     if(i.isupper()):
#         new_string += " " + i
#     else:
#         new_string += i
#
# def solution(s):
#     return ''.join(' ' + c if c.isupper() else c for c in s)
#
# print(new_string)

# recipe = {"flour": 500, "sugar": 200, "eggs": 1}
# available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
#
# def cakes(recipe, available):
#     for key, value in recipe.items():
#         for key2, value2 in available.items():
#             if key == key2:
#
#
#
# print(cakes(recipe, available))


# def get_count(sentence):
#     return sum(1 for x in sentence if x in 'aeiou')
#
# print(get_count('Should count all vowels'))

# from math import sqrt
# def is_prime(num):
#     if num > 1:
#         for i in range(2, int(sqrt(num))+1):
#             if num % i == 0:
#                 return False
#         return True
#     else:
#         return False
#
# print(is_prime(2))

# def bouncing_ball(h, bounce, window):
#     if h < 0 or 0 > bounce > 1 or window > h:
#         return -1
#     count = 1
#     while h > window:
#         h *= bounce
#         if h <= window:
#             break
#         count += 2
#     return count
#
# print(bouncing_ball(2, 0.5, 1))


# def expanded_form(num):
#     return ' + '.join([str(int(v) * 10**k) for k, v in enumerate(str(num)[::-1]) if int(v) != 0][::-1])
#
#
# # def expanded_form(num):
# #     num = list(str(num))
# #     return ' + '.join(x + '0' * (len(num) - y - 1) for y,x in enumerate(num) if x != '0')
#
# print(expanded_form(951753))



# def solution(s):
#     return [s[k:k + 2] if len(s[k:k + 2]) == 2 else s[k:k + 2] + '_' for k in range(0, len(s), 2)]
#
#
# print(solution('abc'))
#
#
# def solution(s):
#     list =[]
#     for k in range(0, len(s), 2):
#         if len(s[k:k+2]) == 2:
#             list.append(s[k:k+2])
#         else:
#             list.append(s[k:k+2] + '_')
#     return list
#
#
# solution('asdfads')


# def solution(n):
#     units_roman = 'I II III IV V VI VII VIII IX'.split()
#     tens_roman = 'X XX XXX XL L LX LXX LXXX XC'.split()
#     hundreads_roman = 'C CC CCC CD D DC DCC DCCC CM'.split()
#     thousands_roman = 'M MM MMM MMMM'
#
#     x = [int(a) for a in str(n)][::-1]
#     r = list()
#     for key, value in enumerate(x):
#         if key == 0:
#             for i in range(1, 10):
#                 if value == i:
#                     r.append(units_roman[i-1])
#         elif key == 1:
#             for i in range(1,10):
#                 if value == i:
#                     r.append(tens_roman[i-1])
#         elif key == 2:
#             for i in range(1, 10):
#                 if value == i:
#                     r.append(hundreads_roman[i-1])
#         else:
#             for i in range(1, 10):
#                 if value == i:
#                     r.append(thousands_roman[i-1])
#     r.reverse()
#     print(''.join(r))
#
#
# def solution(n):
#     units_roman = 'I II III IV V VI VII VIII IX'.split()
#     tens_roman = 'X XX XXX XL L LX LXX LXXX XC'.split()
#     hundreads_roman = 'C CC CCC CD D DC DCC DCCC CM'.split()
#     thousands_roman = 'M MM MMM MMMM'
#     romans = (units_roman, tens_roman, hundreads_roman, thousands_roman)
#
#     x = [int(a) for a in str(n)][::-1]
#     r = list()
#     for key, value in enumerate(x):
#         for i in range(1, 10):
#             if value == i:
#                 if key == 0:
#                     r.append(units_roman[i - 1])
#                 elif key == 1:
#                     r.append(tens_roman[i-1])
#                 elif key == 2:
#                     r.append(hundreads_roman[i-1])
#                 else:
#                     r.append(thousands_roman[i-1])
#     r.reverse()
#     print(''.join(r))
#
#
# def solution(n):
#     units_roman = 'I II III IV V VI VII VIII IX'.split()
#     tens_roman = 'X XX XXX XL L LX LXX LXXX XC'.split()
#     hundreads_roman = 'C CC CCC CD D DC DCC DCCC CM'.split()
#     thousands_roman = 'M MM MMM MMMM'.split()
#     romans = (thousands_roman, hundreads_roman, tens_roman, units_roman)
#     x = [int(a) for a in f'{n:0>4}']
#     print(x)
#     r = list()
#     for key, value in enumerate(x):
#         for i in range(1, 10):
#             if value == i:
#                 r.append(romans[key][i-1])
#     return ''.join(r)
#
# print(solution(4))

# def solution(n):
#     units_roman = 'I II III IV V VI VII VIII IX'.split()
#     tens_roman = 'X XX XXX XL L LX LXX LXXX XC'.split()
#     hundreads_roman = 'C CC CCC CD D DC DCC DCCC CM'.split()
#     thousands_roman = 'M MM MMM MMMM'.split()
#     romans = (thousands_roman, hundreads_roman, tens_roman, units_roman)
#     return ''.join(romans[key][i-1]for key, value in enumerate([int(a) for a in f'{n:0>4}']) for i in range(1, 10) if value == i)
#
#
# print(solution(21))


# units = " I II III IV V VI VII VIII IX".split(" ")
# tens = " X XX XXX XL L LX LXX LXXX XC".split(" ")
# hundreds = " C CC CCC CD D DC DCC DCCC CM".split(" ")
# thousands = " M MM MMM".split(" ")
#
# def solution(n):
#     return thousands[n//1000] + hundreds[n%1000//100] + tens[n%100//10] + units[n%10]

# def rot13(message):
#     d_alpha = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
#     new_message = ''
#     for character in message:
#         if character.isalpha():
#             if character.isupper():
#                 new_message += d_alpha[d_alpha.find(character.lower()) + 13].upper()
#             else:
#                 new_message += d_alpha[d_alpha.find(character) + 13]
#         else:
#             new_message += character
#     return new_message
#
# print(rot13('aA bB zZ 1234 *!?%'))

# def find_even_index(arr):
    # for index, value in enumerate(arr):
    #     if sum(arr[:index:]) == sum(arr[index+1:]):
    #         return index
    # return -1
# print(find_even_index([1,2,3,4,3,2,1]))

# def valid_solution(board):
#     numbers = [int(a) for a in '1 2 3 4 5 6 7 8 9'.split()]
#     #checagem das linhas
#     for x in board:
#         x.sort()
#         if x != numbers:
#             return False
#         #checagem das colunas
#         new_coluna = list()
#         for j in range(9):
#             for i in range(9):
#                 new_coluna.append(board[i][j])
#             new_coluna.sort()
#             if new_coluna != numbers:
#                 return False
#
#
#
# valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
#                                  [6, 7, 2, 1, 9, 0, 3, 4, 9],
#                                  [1, 0, 0, 3, 4, 2, 5, 6, 0],
#                                  [8, 5, 9, 7, 6, 1, 0, 2, 0],
#                                  [4, 2, 6, 8, 5, 3, 7, 9, 1],
#                                  [7, 1, 3, 9, 2, 4, 8, 5, 6],
#                                  [9, 0, 1, 5, 3, 7, 2, 1, 4],
#                                  [2, 8, 7, 4, 1, 9, 6, 3, 5],
#                                  [3, 0, 0, 4, 8, 1, 1, 7, 9]])

# def sum_strings(x, y):
#     int_x, int_y= 0, 0
#     for c in x:
#         int_x = int_x * 10 + ord(c) - ord('0')
#     for c in y:
#         int_y = int_y * 10 + ord(c) - ord('0')
#     return str(int_x + int_y)
#
# print(sum_strings('123', '456'))

# def increment_string(strng):
#     strng_alpha = strng_digit = ''
#     strng = strng[::-1]
#     for key, character in enumerate(strng):
#         if character.isdigit():
#             strng_digit += character
#         else:
#             strng_alpha += strng[key:]
#             break
#     strng_alpha = strng_alpha[::-1]
#     strng_digit = strng_digit[::-1]
#     if strng_digit == '' or strng_digit == '0':
#         return strng_alpha + '1'
#     else:
#         strng_digit = f'{str(int(strng_digit)+1):0>{len(strng_digit)}}'
#     return strng_alpha + strng_digit
#
#
#
# def increment_string(strng):
#     head = strng.rstrip('0123456789')
#     tail = strng[len(head):]
#     if tail == "": return strng+"1"
#     return head + str(int(tail) + 1).zfill(len(tail))
#
#
# print(increment_string("foo09"))


# def remov_nb(n):
#     result = []
#     for a in range(n):
#         for b in range(a+1, n+1):
#             if b in range(n) and a * b == (sum(range(n+1)) - a - b):
#                 result.append((a, b))
#                 result.append((b, a))
#     return result
#
# print(remov_nb(100))


# # essa não passou no tempo
# def remov_nb(n):
#     result = []
#     x = sum(range(n+1))
#     for a in range(n):
#         for b in range(a+1, n+1):
#             if b in range(n) and a * b == x - a - b:
#                 result.append((a, b))
#                 result.append((b, a))
#     return result
#
# # essa passou
# def remov_nb(n):
#     result = []
#     sequence_sum = n * (n + 1) // 2
#     for x in range(1, n + 1):
#         y = (sequence_sum - x) // (x + 1)
#         if y <= n and x * y == (sequence_sum - x - y):
#             result.append((x, y))
#     return result




#from math import sqrt, floor

# # Não passou no tempo
# def list_squared(m, n):
#     results = list()
#     for i in range(m, n+1):
#         divisors = [j**2 for j in range(1, i+1) if i % j == 0]
#         sum_of_squares = sum(divisors)
#         if sum_of_squares % sqrt(sum_of_squares) == 0:
#             results.append([i, sum_of_squares])
#     return results
# from math import sqrt, floor
# def list_squared(m, n):
#     result = []
#     for num in range(m, n + 1):
#         divisors = set()
#         for i in range(1, int(sqrt(num)+1)): #diminui complexidade aqui
#             if num % i == 0:
#                 divisors.add(i**2)
#                 divisors.add(int(num/i)**2)
#         total = sum(divisors)
#         sr = sqrt(total)
#         if sr - floor(sr) == 0: #floor arredonda para baixo (int)
#             result.append([num, total])
#     return result
#
# print(list_squared(1, 250))





# a, b = 2, 9
# print(a%b)  # resto da divisão
# print(a/b)
# print(a//b) # divisão inteira


# def make_readable(seconds):
#     hour = seconds // 3600
#     if hour >= 1:
#         seconds = seconds % 3600
#     minutes = seconds // 60
#     if minutes >= 1:
#         seconds = seconds % 60
#     return f'{hour:0>2}:{minutes:0>2}:{seconds:0>2}'
#
# print(make_readable(359999))

# def dbl_linear(n):
#     dbl_list = [1, 3, 4]
#     for x in range(3, n+1):
#         y = 2 * dbl_list[x-2] + 1
#         z = 3 * dbl_list[x-2] + 1
#         if y not in dbl_list:
#             dbl_list.append(y)
#         if z not in dbl_list:
#             dbl_list.append(z)
#         dbl_list = sorted(dbl_list)
#     return (dbl_list[n])
#
# print(dbl_linear(10))
#
#
# def dbl_linear(n):
#     dbl_list = [1, 3, 4]
#     y = (2*dbl_list[x-2]+1 for x in range(3, n+1))
#     z = (3*dbl_list[x-2]+1 for x in range(3, n+1))
#     print(tuple(y))
#
#
# print(dbl_linear(10))


# def rgb(r, g, b):
#     answer = ''
#     for x in (r,g,b):
#         if x > 255:
#             x = 255
#         if x < 0:
#             x = 0
#         answer += f'{hex(x)[2:]:0>2}'.upper()
#     return answer
#
# print(rgb(-20, 275, 125))
#
# print(hex(-20))


# import numpy as np
#
# def determinant(matrix):
#     return round(np.linalg.det(matrix))
#
#
# print(determinant([[2, 4, 2],
#                    [3, 1, 1],
#                    [1, 2, 0]]
#                   ))

import string
string.ljust(width=30,s='Mary had a little lamb')