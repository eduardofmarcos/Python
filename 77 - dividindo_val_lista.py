lista = []
pares = []
impares = []
while True:
    n = int(input('Digite um numero: '))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    elif n % 2 != 0:
        impares.append(n)
    opcao = str(input('deseja continuar?')).strip().upper()
    if opcao == 'S':
        True
    else:
        break

print('Lista total {}'.format(sorted(lista)))
print('Lista de pares: {}'.format(pares))
print('Lista de impares: {}'.format(impares))