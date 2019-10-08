numero = int(input('Insira o numero a ser multiplicado: '))
multiplicador = int(input('Insira um numero multiplicante: '))

i = 0

for i in range(multiplicador+1):
    r = i * numero
    print('{} * {} = {}'.format(i, numero, r))
