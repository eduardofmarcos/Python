total = 0
milreais = 0
lista = []
nomeProduto = []
opcao = ''
while True:
    while True:
        produto = str(input('Digite o nome do produto: ')).strip().upper()
        if produto.isalpha():
            break
    while True:
        preco = (input('Digite o preco do produto: '))
        if preco.isalpha():
            True
        else:
            preco = float(preco)
            break

    nomeProduto.append(produto)
    lista.append(preco)

    total = total + preco
    if preco > 1000:
        milreais = milreais + 1

    while True:
        opcao = str(input('Voce deseja continuar? S sim ou N nao: ')).strip().upper()
        if opcao == 'S' or opcao == 'N':
            break
    if opcao == 'N':
        break

menor = lista.index(min(lista))
print('A soma dos produtos é: {}, o mais barato é {} e teve {} acima de 1000 reais.'.format(total, nomeProduto[menor], milreais))
