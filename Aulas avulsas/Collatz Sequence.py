def collatz(number):
    if number % 2 == 0:
        new_number = number // 2
        print(new_number, end=' ')
    else:
        new_number = 3 * number + 1
        print(new_number, end=' ')
    return new_number


n = ''
while n != 1:
    while n == '':
        n = int(input('Digite um número inteiro diferente de 1: '))
        print(n, end=' ')
    n = collatz(n)
