import random
numeros = []


def sorteio():
    for i in range(0, 5):
        n = (random.randint(1, 100))
        numeros.append(n)
    print('A lista de numeros aleatorios é: {} '.format(numeros))


def somapares():
    s=0
    for num in numeros:
        if num % 2 == 0:
            s = s+num
    print('A soma de numeros pares dentro da lista aleatoria {} é {} '.format(numeros, s))


sorteio()
somapares()
