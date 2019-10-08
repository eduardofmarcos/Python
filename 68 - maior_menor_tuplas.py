import random
n1 = random.randint(0, 5)
n2 = random.randint(0, 5)
n3 = random.randint(0, 5)
n4 = random.randint(0, 5)
n5 = random.randint(0, 5)
numeros = (n1, n2, n3, n4, n5)
min = (min(numeros))
max = (max(numeros))
print('Dos numeros abaixo: ')
for c in range(len(numeros)):
    n = numeros[c]
    print(n, end= ' ')
print('\nO menor numero é {}'.format(min))
print('E o maior é {}'.format(max))
