def maior(*numero):      #parametros empacotados
    maior = 0
    print('Dentre os valores: ')
    for n in numero:
        if n > maior:
            maior = n
        print(n, end=' - ')
    print('')
    print('O maior valor é: {}'.format(maior))
    print('--------------------------------')
maior(10, 15, 20,191,  2, 1, 190)
maior(12,3,5,10)

