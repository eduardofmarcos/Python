dados = dict()
gols = []
soma = 0
dados['nome'] = str(input('Digite o nome do jogador: '))
quantidadepartidas = int(input('Digite a quantidade de partidas: '))
for i in range(0, quantidadepartidas):
    ngoals = int(input('Digite a quantidade de gols na partida {}: '.format(i+1)))
    soma  = soma + ngoals
    gols.append(ngoals)
dados['gols'] = gols
dados['total'] = soma
print(dados)
print('=-'*20)
print('')
for k, v in dados.items():
    print('o campo {} tem valor {}.'.format(k, v))
print('')
print('=-'*20)
print('')
print('O jogador {} jogou {} partidas.'.format(dados['nome'], quantidadepartidas))
for i in range(0, quantidadepartidas):
    print('=> Na partida {} fez {}'.format(i+1, dados['gols'][i]))
print('Foi um total de {} gols!'.format(dados['total']))