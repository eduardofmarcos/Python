numeros = []
maiores = []
menores = []
for contador in range(0, 5):
    valor = int(input('Digite um valor: '))
    numeros.append(valor)
cont = 0
maior = max(numeros)
menor = min(numeros)
for numero in numeros:
    cont = cont + 1
    if numero == maior:
        maiores.append(cont)
    if numero == menor:
        menores.append(cont)
    print('O numero {} esta na posicao {}'.format(numero, cont))
print('o maior numero é {} e esta na posicao {}'.format(maior, maiores))
print('o menor numero é {} e esta na posicao {}'.format(menor, menores))







