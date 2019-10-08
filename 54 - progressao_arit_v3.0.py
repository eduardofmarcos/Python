t = 0
opcao = ''
while opcao != 'Sair':
    termo1 = int(input('Digite o primiero termo: '))
    razao = int(input('Digite a razao: '))
    nt = int(input('Digite o numero de termos que voce deseja: '))

    while t != (razao * nt):
        t = t + razao
        p = termo1 + t
        print(p, end='> ')

    opcao = str(input('Deseja continuar? [S] ou tecle enter para sair: ')).strip().upper()
    if opcao == 'S':
        t = 0
        p = 0
        razao = 0
        print('Preencha os campos!')
    else:
        opcao = 'Sair'
        print('Obrigado!')



