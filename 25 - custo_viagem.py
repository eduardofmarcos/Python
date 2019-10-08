dis = float(input('Digite a distancia em KM: '))

if dis <= 200:
    val = dis * 0.50
    print('O valor da passagem é R${:.2f} reais'.format(val))
else:
    val = dis * 0.45
    print('O valor da passagem é: R${:.2f} reais'.format(val))
