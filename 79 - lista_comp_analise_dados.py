listaprincipal = []
dados = []
maxpeso = []
minpeso = []
c = 0
while True:
    nome = str(input('Digite seu nome: ')).strip().upper()
    peso = float(input('Digite seu peso: '))
    dados.append(nome)
    dados.append(peso)
    listaprincipal.append(dados[:])
    dados.clear()
    c = c + 1
    opcao = str(input('Deseja continuar? [S] sim // [N] nao: ')).strip().upper()
    while opcao not in 'SNsn':
        opcao = str(input('Deseja continuar? [S] sim // [N] nao: ')).strip().upper()
    if opcao == 'S':
        True
    else:
        break

def my_max_by_weight(sequence):
    if not sequence:
        raise ValueError('empty sequence')

    maximum = sequence[0]

    for item in sequence:

        if item[1] > maximum[1]:
            maximum = item

    return maximum

def my_min_by_weight(sequence):
    if not sequence:
        raise ValueError('empty sequence')

    minimum = sequence[0]

    for item in sequence:

        if item[1] < minimum[1]:
            minimum = item

    return minimum
maxi = my_max_by_weight(listaprincipal)
max = maxi[1]
mini = my_min_by_weight(listaprincipal)
min = mini[1]
for listainterna in listaprincipal:
    if listainterna[1] == max:
        maxpeso.append(listainterna[0])
    if listainterna[1] == min:
        minpeso.append(listainterna[0])
print('Ao todo voce cadastrou {} pessoas'.format(c))
print('O maior peso foi {} de {}'.format(max, maxpeso))
print('O menor peso foi {} de {}'.format(min, minpeso))

