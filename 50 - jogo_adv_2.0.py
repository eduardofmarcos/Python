import random
tentativas = 0
numero = 0
numPC = 1

while numero != numPC:
    numero = int(input('Digite um numero: '))
    numPC = random.randint(0, 10)
    tentativas = tentativas + 1
    print('----'*10)
    print('Eu escolhi {}'.format(numPC))
print('Levou {} tentativas pra voce adivinhar!'.format(tentativas))

