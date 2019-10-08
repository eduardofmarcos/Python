time = ('Flamengo','Palmeiras','Santos','Internacional','Corinthians','Sao Paulo','Bahia','Gremio','Atletico','Botafogo','Atletico-PR','Vasco da Gama','Ceara SC','Fortaleza','Goias','Fluminense','Cruzeiro','CSA','Chapecoense','Avai')
chape = ''
opcao = str(input('Digite o time que quer achar: ')).capitalize().strip()
print(time)
print(time[:5])
print(time[-4:])
print(sorted(time))
for ti in range(0, len(time)):
    if time[ti] == opcao:
        print('O {} procurado esta na posição {} do ranking'.format(opcao, ti+1))
