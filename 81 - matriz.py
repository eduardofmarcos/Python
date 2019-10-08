matrix = [[], [], [], [], [], [], [], [], []]
segundalinha = []
t = pares = somatres = 0
for l in range(0, 3):
    for c in range(0, 3):
        p = int(input(('Digite a posição-> {}.{}: '.format(l, c))))
        if p % 2 == 0:
            pares = pares + p
        if c == 2:
            somatres = somatres + p
        if l == 1:
            segundalinha.append(p)
        t = t + 1
        matrix[t-1].append(p)
print(matrix[0], matrix[1], matrix[2])
print(matrix[3], matrix[4], matrix[5])
print(matrix[6], matrix[7], matrix[8])
print('A soma dos numeros pares é {}'.format(pares))
print('A soma dos numeros da terceira coluna é {}'.format(somatres))
print('O maior valor da segundalinha é: {}'.format(max(segundalinha)))


