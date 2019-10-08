import random

num = random.randint(0, 5)

numcheck = int(input('Digite um numero de 1 a 5 para comparar com o numero do PC: '))


if num == numcheck:
    print('Voce acertou!')

elif num != numcheck and numcheck >= 0 and numcheck <= 5:
    print('Voce errou!')

else:
    print('Apenas numero entre 1 e 5, por favor')

