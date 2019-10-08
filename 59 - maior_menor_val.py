c = 0
s = 0
lista = []
opcao = ''
while opcao != 'E':
    while opcao != 'E':
        numero = float(input('Digite um numero: '))
        c = c + 1
        s = s + numero
        lista.append(numero)
        opcao = input('Voce deseja continuar? ')
        if opcao == 'S':
            opcao != 'E'
        else:
            opcao == 'E'
media = s / c
maxi = max(lista)
mini = min(lista)
print(media)
print(lista)
print(maxi)
print(mini)


