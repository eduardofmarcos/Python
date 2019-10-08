temp = float(input('Digite a temperatura: '))
opt = float(input('Digite 1 para C>>F, ou 2 para F>>C: '))

if opt == 1:
    convert = (temp * 5/8) + 32
    print('A temperatura escolhida {:.1f} em C é {:.1f} em F'.format(temp, convert))
elif opt == 2:
    convert = (temp -32) * 5/9
    print('A temperatura escolhida {:.1f} em F é {:.1f} em C'.format(temp, convert))
else:
    print('Selecione a opção 1 para C>>F ou 2 para F>>C')



