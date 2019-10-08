def contador(inicio, fim, passo):
    if inicio < fim:
        if passo == 0:
            passo = 1
        for i in range(inicio, fim+1, passo):
            print(i, end=' -> ')
    elif inicio > fim and passo < 0:
        passo = passo * -1
        for i in range(inicio, fim-passo, -(passo)):
            print(i, end=' -> ')
    elif inicio > fim:
        if passo == 0:
            passo = 1
        for i in range(inicio, fim-passo, -(passo)):
            print(i, end=' ->  ')


contador(0, 10, 1)
print('')
contador(10, 0, 2)
print('')
inicio = int(input('Digite o inicio: '))
fim = int(input('Digite o fim: '))
passo = int(input('Digite o passo: '))
contador(inicio, fim, passo)
