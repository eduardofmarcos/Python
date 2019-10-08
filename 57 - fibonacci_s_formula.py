termo = int(input('Digite um termo: '))
t1 = 0
t2 = 1
contador = 0
t3 = t1 + t2
print(t3, end='> ')
while contador != termo-1:
    contador = contador + 1
    t3 = t1 + t2
    print(t3, end='> ')
    t1 = t2
    t2 = t3




