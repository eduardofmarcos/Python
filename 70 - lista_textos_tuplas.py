tupla = ('Abacaxi','1.50', 'Abacate','2.30', 'Caneta', '3.20', 'Papel', '4.50')
cont = 0
for cont in range(len(tupla)):
    if cont % 2 == 0:
        print(' {0:.<20} R$'.format(tupla[cont]), end=' ')
    if cont % 2 == 1:
        print(tupla[cont])

