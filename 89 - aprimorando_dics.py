dados = dict()
gols = []
cadastro = []
soma = t = 0
golsjogador = []
golpartida = []
partida = []
while True:
    dados['nome'] = str(input('Digite o nome do jogador: '))
    quantidadepartidas = int(input('Digite a quantidade de partidas: '))
    for i in range(0, quantidadepartidas):
        ngoals = int(input('Digite a quantidade de gols na partida {}: '.format(i)))
        partida.append(i)
        golpartida.append(ngoals)
        soma  = soma + ngoals
        gols.append(ngoals)
    dados['gols'] = gols[:]
    dados['total'] = soma
    dados['partida'] = partida[:]
    dados['golpartida'] = golpartida[:]
    cadastro.append(dados.copy())
    gols.clear()
    soma = 0
    opt = str(input('Deseja continuar? [S] - sim// [N] - não: ')).upper()[0]
    if opt in 'N':
        break
    else:
        gols.clear()
        partida.clear()
        golpartida.clear()
print('Cod -- Nome -- Gols -- Total')
for jogador in cadastro:
    t = t + 1
    print(t-1, cadastro[t-1]['nome'], cadastro[t-1]['gols'], cadastro[t-1]['total'])
print('=-'*30)
print('')
while True:
    opcao = int(input('Digite o codigo do jogador (digite 888 para sair): '))
    if opcao == 888:
        print('Obrigado!')
        break
    else:
        for n, dado in enumerate(cadastro):
            if opcao == n:
                print('Levantamento do jogado {}: '.format(dado['nome']))
                for i in range(len(dado['partida'])):
                    print('----> Na partida {} ele fez {} gols.'.format(dado['partida'][i], dado['golpartida'][i]))


































































#for k, v in dados.items():
 #   print('o campo {} tem valor {}.'.format(k, v))
#print('')
#print('=-'*20)
#print('')
#print('O jogador {} jogou {} partidas.'.format(dados['nome'], quantidadepartidas))
#for i in range(0, quantidadepartidas):
 #   print('=> Na partida {} fez {}'.format(i+1, dados['gols'][i]))
#print('Foi um total de {} gols!'.format(dados['total']))