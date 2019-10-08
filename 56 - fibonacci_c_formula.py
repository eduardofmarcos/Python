termo = int(input('Digite um termo: '))
c = 0
t = 0
while c!= termo:
    c = c + 1
    t = t + 1
    x = (1.618034)**t - (1-1.618034)**t
    raiz = 5**0.5
    fibo = x / raiz
    print(round(fibo), end='> ')
print('\nO termo {} de fibonacci é: {} '.format(termo,round(fibo)))

