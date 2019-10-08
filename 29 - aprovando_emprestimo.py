nome = str(input('Digite seu nome: ')).strip()
sal = float(input('Digite seu salario: '))
valor = float(input('Digite o valor do imovel:'))
prazo = int(input('Digite o valor do prazo em anos: '))


prazoMes = prazo*12
valorParcela = valor / (prazoMes)

if valorParcela <= (sal * 0.3):
    print('Seu financiamento foi aprovado!')

elif valorParcela > (sal * 0.3):
    dif = valorParcela - (sal*0.3)

    print('Seu financiamento foi negado, para aprovar necessita de mais R$: {:.2f} de renda'.format(dif))
