frase = str(input('Digite uma frase: ')).strip().lower()
nova_frase = frase.replace(' ', '')

tamanho = len(nova_frase)
print(tamanho)
for contador in range(0, tamanho):
    linha1 = nova_frase[contador]
    print(linha1, end='>')
print('////')

for contador1 in range(tamanho - 1, -1, -1):
    linha2 = nova_frase[contador1]
    print(linha2, end='>')
print('////')

if linha1 == linha2:
    print('Temos um palindroma!')
else:
    print('Não temos!')






