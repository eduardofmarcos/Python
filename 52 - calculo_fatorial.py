numero = int(input('Digite um numero: '))
### FOR
r = 1
for c in range(1, numero + 1):
    r = (c * r)
print('O fatorial de {} é: {} '.format(numero, r))
####### WHILE
t = 0
r = 1
while t != numero:
    t = t + 1
    r = (t * r)
print('O fatorial de {} é: {}'.format(numero, r))
