numero = int(input('Digite um numero inteiro: '))

opcao = input(('Entendi! voce que transformar esse numero para que base? 1 - Binario; 2 - octal e 3 - hexadecimal: '))

if opcao == '1':
    binario = bin(numero)[2:].zfill(10)
    print(binario)

elif opcao == '2':
    octal = oct(numero)
    print(octal)


elif opcao == '3':
    hexa = hex(numero)
    print(hexa)

else:
    print('Digite um numero entre 1 e 3')