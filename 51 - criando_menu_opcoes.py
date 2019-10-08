import time

opcao = ''

while opcao != '5' and opcao != 'S':
    numero1 = float(input('Digite o primeiro numero: '))
    numero2 = float(input('Digite o segundo numero: '))

    print('-='*20)
    print('Selecione a opção desejada:\n'
          '[1] - Somar\n'
          '[2] - multiplicar\n'
          '[3] - Maior\n'
          '[4] - Novos numeros\n'
          '[5] - Sair do programa\n')
    print('-=' * 20)
    opcao = (input('Digite a opção desejada: '))

    if opcao == '1':
        soma = numero1 + numero2
        print(soma)
        print('-=' * 20)
        opcao = input('Digite [S] para sair ou Enter para continuar: ')
    elif opcao == '2':
        multiplicacao = numero1 * numero2
        print(multiplicacao)
        print('-=' * 20)
        opcao = input('Digite [S] para sair ou Enter para continuar: ')
    elif opcao == '3':
        if numero1 > numero2:
            print(numero1)
            print('-=' * 20)
            opcao = input('Digite [S] para sair ou Enter para continuar: ')
        elif numero1 == numero2:
            print('Numeros iguais!')
            opcao = input('Digite [S] para sair ou Enter para continuar: ')
        else:
            print(numero2)
            print('-=' * 20)
            opcao = input('Digite [S] para sair ou Enter para continuar: ')
    elif opcao == '4':
        print('-=' * 20)
        print('Escolha os numeros novamente: ')
    elif opcao == '5':
        print('-=' * 20)
        print('Saindo do programa em: ')
        time.sleep(2)

    else:
        print('Opcao invalida')
        print('-=' * 20)
print('-='*20)
print('Obrigado por participar')
