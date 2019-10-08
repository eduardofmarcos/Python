soma = 0
contador = 0
numero = 0

while numero != 888:
    numero = int(input('Digite um numero: '))
    if numero == 888:
        break
    contador += 1
    soma += numero
print('Foi digitado {} numeros e a soma entre eles é: {}'.format(contador, soma))


