import random
aposta = []
jogo = []
c = 0
numerojogos = int(input('Quantos jogos quer que eu palpite? '))
for i in range(0, numerojogos):
    jogo = random.sample(range(60), 6)
    aposta.append(jogo[:])
for ap in aposta:
    print('Jogo {}: {}'.format(c + 1, sorted(ap)))
    c = c + 1
