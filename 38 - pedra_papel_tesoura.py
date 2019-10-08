import random

print('--'*40)
print('Digite um valor: \n'
      '1 - Pedra\n'
      '2 - Papel\n'
      '3 - Tesoura')
print('--'*40)
numeroUser = int(input('Escolha a opcao acima: '))

if numeroUser > 0 and numeroUser < 4:

    if numeroUser == 1:
        numeroUser = 'Pedra'
    elif numeroUser == 2:
        numeroUser = 'Papel'
    elif numeroUser == 3:
        numeroUser = 'Tesoura'


    numeroPC = random.randint(1,3)



    if numeroPC == 1:
        numeroPC ='Pedra'
    elif numeroPC == 2:
        numeroPC = 'Papel'
    elif numeroPC == 3:
        numeroPC = 'Tesoura'
    print('--'*40)
    print('Voce escolheu {} e o computador escolheu {}'.format(numeroUser, numeroPC))
    print('--'*40)

    if numeroUser == 'Pedra' and numeroPC == 'Tesoura':
        print('Voce ganhou')
    elif numeroUser == 'Tesoura' and numeroPC == 'Papel':
        print('Voce ganhou')
    elif numeroUser == 'Papel' and numeroPC == 'Pedra':
        print('Voce ganhou')

    elif numeroPC == 'Pedra' and numeroUser == 'Tesoura':
        print('PC ganhou')
    elif numeroPC == 'Tesoura' and numeroUser == 'Papel':
        print('PC ganhou')
    elif numeroPC == 'Papel' and numeroUser == 'Pedra':
        print('PC ganhou')

    elif numeroUser == 'Pedra' and numeroPC == 'Pedra':
        print('Houve um empate')
    elif numeroUser == 'Tesoura' and numeroPC == 'Tesoura':
        print('Houve um empate')
    elif numeroUser == 'Papel' and numeroPC == 'Papel':
        print('Houve um empate')

else:
    print('Escolha uma opcao de 1 a 3.')



