numero = int(input('Digite um numero ok: '))
x = 0
if numero != 0 and numero != 1:
    for contador in range(1, numero+1):
        if numero % contador == 0:
            x = x + 1
    if x > 2:
        print('O numero nao é primo')
    else:
        print('O numero é primo')
else:
    print('O numero nao é primo')
