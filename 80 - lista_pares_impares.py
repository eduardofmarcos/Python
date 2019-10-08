listaPrincipal = []
listapares = []
listaimpares = []
for c in range(0, 7):
    numero = int(input('Digite um numero: '))
    if numero % 2 == 0:
        listapares.append(numero)
    if numero % 2 != 0:
        listaimpares.append(numero)
listaPrincipal.append(listapares[:])
listaPrincipal.append(listaimpares[:])
print('Pares: {}'.format(sorted(listaPrincipal[0])))
print('Impares: {}'.format(sorted(listaPrincipal[1])))

