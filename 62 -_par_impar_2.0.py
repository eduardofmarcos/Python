import random
import time
c = 0
opcao = ''
pi = ''
while opcao == pi:
    computador = random.randint(0, 5)
    jogador = int(input('Digite um numero: '))
    print('-='*20)
    pi = computador + jogador
    if pi % 2 == 0:
        pi = 'par'
    else:
        pi = 'impar'
    opcao = str(input('[P] - para par, [I] - para impar: ')).lower()
    print('=-'*20)
    print('Processando...')
    time.sleep(1)
    print('Deu {}!'.format(pi))
    if opcao == 'p':
        opcao = 'par'
    else:
        opcao = 'impar'

    if opcao == pi:
        c = c+1
        print('Voce escolheu {}! Voce ganhou!'.format(opcao))
    else:
        print('Voce escolheu {}! Voce perdeu!'.format(opcao))
print('=-'*20)
print('Voce ganhou {} vezes consecutivas'.format(c))
