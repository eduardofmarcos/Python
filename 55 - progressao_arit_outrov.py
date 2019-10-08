t = 0
opcao = ''

while opcao != 'Sair':
    t = 0
    p = 0
    nt = 0

    termo1 = int(input('Digite o primeiro termo ou "0" para sair: '))
    if termo1 != 0:
        razao = int(input('Digite a razao: '))
        nt = int(input('Digite o numero de termos que voce deseja: '))

        while t != (razao * nt):
            t = t + razao
            p = termo1 + t
            print(p, end='> ')

        opcao = str(input('Deseja continuar? [S] ou tecle enter para sair: ')).strip().upper()
        if opcao == 'S':
            nt = int(input('Digite o numero de termos ou "0" para sair: '))
            if nt != 0:
                t = 0
                p = 0
                while t != (razao * nt):
                    t = t + razao
                    p = termo1 + t
                    print(p, end='> ')
                if opcao == 'S':
                    print('\nVamos novamente!')
            else:
                opcao = 'Sair'
                print('Obrigado!')
        else:
            opcao = 'Sair'
            print('Obrigado!')
    else:
        opcao ='Sair'
        print('Obrigado!')




