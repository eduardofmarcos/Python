def ficha(nome='', gol=''):
    if nome == '':
        nome = '<desconhecido>'
    if gol.isnumeric():
        gol = int(gol)
    else:
        gol = 0
    return 'O {} fez {} gols no campeonato'.format(nome, gol)
nome = str(input('Digite o nome: '))
gol = str(input('Digite o gol: '))
print(ficha(nome, gol))




