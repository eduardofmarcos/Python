#ex010>>> Crie um programa que leia quanto uma pessoa tem na carteira e mostre quantos dolares pode comprar,
#Dolar: 3,27

v = float(input('Valor na carteira: '))
c = float(input('Valor do cambio: '))

print('Com esse montante voce consegue comprar: {:.2f} dolares'.format(v/c))
