# ex009>>> Ler um numero inteiro qualquer e mostre sua tabuada

n = int(input('Digite um numero:'))
r = int(input('Digite o range: '))

i = 0

for i in range(r+1): #para o index i no alcance no range.
    t = n*i
    print('{:2} x {:2} = {:2}'.format(i, n, t))

