import time
inicio = int(input('Digite o inicio: '))
fim = int(input('Digite o fim: '))

for c in range(inicio, fim - 1, -1):
    time.sleep(1)
    print(c)
print('FIM')
