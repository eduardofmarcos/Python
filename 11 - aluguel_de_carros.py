km = float(input('Digite a kmmetragem rodada: '))
dias = int(input('Digite a quantidade de dias: '))

total = (km * 0.15) + (dias * 60)

print('O total a pagar pelo aluguel será de R$: {:.2f}'.format(total))

