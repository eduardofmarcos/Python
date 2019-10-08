t = 0
c = 0
n = 0
while n != 888:
    n = int(input('Digite um numero: ou [888]: '))
    c = c + 1
    t = t + n
    if n == 888:
        nt = t - 888
print('Foi informado {} numeros e a soma deles é {}'.format(c-1, nt))
