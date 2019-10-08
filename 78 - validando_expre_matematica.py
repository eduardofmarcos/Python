n = str(input('Expressao: '))
e = r = 0
for l in n:
    if l == ('('):
        e = e + 1
    if l == (')'):
        r = r +1
if e != r:
    print('Expressao Invalida')
if e == r:
    print('Expressao VALIDA')
