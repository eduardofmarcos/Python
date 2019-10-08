sal = float(input('Digite o salario: '))

if sal > 1250:
    acres = (sal * 0.10)
    salfinal = sal + acres
    print('0 salario final é {}'.format(salfinal))
else:
    acres = (sal * 0.15)
    salfinal = sal + acres
    print('O salario final é {}'.format(salfinal))
    