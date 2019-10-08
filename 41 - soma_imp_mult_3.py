inicio = int(input('Digite o inicio: '))
fim = int(input('Digite o fim: '))
soma = 0
for c in range(inicio, fim+1):
    if c % 2 != 0 and c % 3 == 0:
        soma = soma + c
        print(c)
print('=-'*20)
print(soma)
