contadorPessoas = 0
contadorHomens = 0
contadorMulheres = 0
opcao = ''
sexo = ''
idade = 0
while True:
    print('=-'*20)
    while True:
        nome = str(input('Digite o nome: ')).strip().upper()
        if nome.isalpha():
            break
    while True:
        idade = (input('Digite a idade: '))
        if idade.isnumeric():
            idade = int(idade)
            break
    while True:
        sexo = str(input('Digite o sexo: [F] para feminino - [M] para masculino: ')).strip().upper()
        if sexo == 'M' or sexo == 'F':
            break
    if idade > 18:
        contadorPessoas = contadorPessoas + 1
    elif sexo == 'M':
        contadorHomens = contadorHomens + 1
    elif idade < 20 and sexo == 'F':
        contadorMulheres = contadorMulheres + 1
    print('-='*20)
    while True:
        opcao = str(input('Voce deseja cadastrar mais uma pessoa? [S] para sim, [N] para não: ')).strip().upper()
        if opcao == 'S' or opcao == 'N':
            break
    if opcao == 'N':
        break
print('-='*20)
print('Numero de mulheres abaixo de 20 anos: {}, Homens: {}, Maiores de idade: {}'. format(contadorMulheres, contadorHomens, contadorPessoas))







