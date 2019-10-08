n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
n4 = int(input('Digite o quarto numero: '))
numeros = (n1, n2, n3, n4)
nove = tres = pares = 0
for num in numeros:
    if num == 9:
        nove = numeros.count(9)
    if num == 3:
        tres = numeros.index(3)
    if num % 2 == 0:
        pares = num
        print(pares, end=' ')
if pares > 0:
    print('\nOs numeros acimas são pares.')
if nove == 0:
    print('\nNao ha nove nessa lista')
else:
    print('Tem {} noves nessa lista'.format(nove))
if tres == 0:
    print('Nao ha tres nessa lista')
else:
    print('O numero tres fica na {} posição'.format(tres+1))




