import random

n1 = input('Digite o nome do primeiro: ')
n2 = input('Digite o nome do segundo: ')
n3 = input('Digite o nome do terceiro: ')
n4 = input('Digite o nome do quarto: ')

lista = [n1, n2, n3, n4]

f1, f2, f3, f4 = random.sample(lista, 4)

print('Primeiro lugar é: {}, segundo lugar é: {}, terceiro lugar é: {} e o quarto lugar é: {}'.format(f1, f2, f3, f4))




