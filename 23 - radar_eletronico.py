vel = float(input('Digite a velocidade de um carro: '))

if vel <= 80.0:
    print('\033[2;34;46mDentro do limite\033[m')
else:
    ex = vel - 80.0
    m = ex * 7
    print('Velocidade foi de {} e excedeu o limite de 80km/h por {} km/h. Multa sera de R${} reais'.format(vel, ex, m))
