import random
import time
from operator import itemgetter
tabela = []
jogos = dict()
t = 1
for i in range(0, 4):
    jogos['jogador'] = i+1
    jogos['aposta'] = random.randint(1, 6)
    time.sleep(1)
    print('O jogador {} tirou a aposta {}!'.format(jogos['jogador'], jogos['aposta']))
    tabela.append(jogos.copy())
    jogos.clear()
print('=-'*20)
print('O ranking ficou assim:')
print('=-'*20)
tabelaalinhada = sorted(tabela, key=itemgetter('aposta'), reverse=True)
for j in tabelaalinhada:
    print('O jogador {} ficou na posição {} com a aposta: {}'.format(j['jogador'], t, j['aposta']))
    t = t + 1
    time.sleep(0.5)

