termo1 = int(input('Digite o primiero termo: '))
razao = int(input('Digite a razao: '))
t = 0

print('Os 10 primeiros termos de uma P.A. com primeiro termo {} e com razão {} são:'.format(termo1, razao))
while t != (razao*10):
    t = t + razao
    p = termo1 + t
    print(p, end='> ')

