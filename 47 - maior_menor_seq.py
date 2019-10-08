lista = []

for contador in range(0, 5):
    peso = float(input('Digite o seu peso: '))
    lista.append(peso)

print([lista])

print('O Menor valor peso da lista é: {}'.format(min(lista)))
print('O Maior valor peso da lista é: {}'.format(max(lista)))
