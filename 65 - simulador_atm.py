valor = int(input('Digite o valor a ser sacado: '))
cinquenta = vinte = dez = cinco = um = 0
while True:
    resto = valor
    while True:
        if resto < 50:
            break
        cinquenta = cinquenta + 1
        resto = resto - 50
        if resto < 50 or resto == 0:
            break
    while True:
        if resto == 0 or resto < 20:
            break
        vinte = vinte +1
        resto = resto - 20
        if resto < 20 or resto == 0:
            break
    while True:
        if resto == 0 or resto < 10:
            break
        dez = dez + 1
        resto = resto - 10
        if resto < 10 or resto == 0:
            break
    while True:
        if resto == 0 or resto < 5:
            break
        cinco = cinco + 1
        resto = resto - 5
        if resto < 5 or resto == 0:
            break
    while True:
        if resto == 0 or resto < 1:
            break
        um = um + 1
        resto = resto - 1
        if resto < 1 or resto == 0:
            break
    break
print('''Será entregue {} cedulas de 50 reais,
{} de 20 reais
{} de 10 reais
{} de 5 reais
{} de 1 real'''.format(cinquenta, vinte, dez, cinco, um))
