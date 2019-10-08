ano = (input('Digite um ano: '))

p1 = ano[2]
p2 = ano[3]

if p1 == 0 and p2 == 0:
    n2 = int(ano) % 400
    n3 = int(ano) % 100
    if n2 == 0 and n3 != 0:
        print('O ano de {} é bissexto'.format(ano))

if p1 != 0 or p2 != 0:
    n1 = int(ano) % 4
    if n1 == 0:
            print('O ano de {} é bissexto'.format(ano))
    else:
            print('O ano de {} não é bissexto'.format(ano))
