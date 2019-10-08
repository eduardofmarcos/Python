dados = dict()
c = somaidade = 0
cadastro = []
while True:
    dados['nome'] = str(input('Digite seu nome: ')).upper().strip()
    dados['idade'] = int(input('Digite sua idade: '))
    dados['sexo'] = str(input('Digite seu sexo [M] - Masculino// [F] - Feminino: ')).upper().strip()[0]
    cadastro.append(dados.copy())
    somaidade = somaidade + dados['idade']
    dados.clear()
    c = c + 1
    opt = str(input('Deseja continuar [S] para sim // [N] para não: ')).upper()[0]
    if opt in 'N':
        break
media = somaidade / c
print('=-'*20)
print('O numero de pessoas cadastradas é {}.'.format(c))
print('O media da idade do grupo é {} anos.'.format(media))
print('=-'*20)
print('Cadastro de pessoas do sexo feminino: ')
for pessoa in cadastro:     # lista os dicionarios
    if pessoa['sexo'] == 'F':   # pegas os indices literais dos dicionarios
        for k, v in pessoa.items(): # pega as chaves e valores dos dicionasrios e lista
            print('O campo {} tem o valor {} '.format(k, v,))
    print('=-'*20)
print('Cadastros de pessoas com idade acima da media: ')
for pessoa in cadastro:
    if pessoa['idade'] > media:
        for k, v in pessoa.items():
            print('O campo {} tem o valor {} '.format(k, v,))
    print('=-' * 20)