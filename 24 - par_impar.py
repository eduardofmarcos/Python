import math

n = int(input('Digite um numero inteiro: '))

r = n % 2

if r == 0:
    print('{} é par'.format(n))
else:
    print('{} é impar'.format(n))

