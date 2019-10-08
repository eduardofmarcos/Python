numero = 0
c = 0
while numero >= 0:
    numero = int(input('Quer ver a tabuada de que valor? '))
    print('-='*20)
    if numero < 0:
        break
    for c in range(0,11):
        produto = numero * c
        print('{} x {}: {}'.format(numero, c, produto))
    print('-=' * 20)
print('Obrigado!')