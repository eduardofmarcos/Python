inicio = int(input('Digite o inicio da contagem: '))
fim = int(input('Digite o fim da contagem: '))

if inicio % 2 == 0:
    for c in range(inicio, fim+1, 2):
        print(c)
else:
    print('O numero nao é par')
print('FIM')
