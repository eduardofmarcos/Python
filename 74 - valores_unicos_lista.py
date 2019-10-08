lista = []
valor = 0
while True:
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
        print('Valor adicionado!')
        opcao = str(input('Quer continuar: [S] para sim, [N] para nao: ')).strip().upper()[0]
        if opcao == 'S':
            True
        else:
            break
    else:
        print('Valor ja adicionado!')
        opcao = str(input('Quer continuar: [S] para sim, [N] para nao: ')).strip().upper()[0]
        if opcao == "S":
            True
        else:
            break
print('Os valores adicionados foram: {}'.format(sorted(lista)))





