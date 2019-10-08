import datetime

nome = str(input('Digite seu nome: ')).strip()
ano = int(input('Digite o ano de nascimento: '))

agora = datetime.datetime.now()
anohoje = agora.year

situacao = anohoje - ano

if situacao > 18:
    excesso = situacao - 18
    anoexcesso = anohoje - excesso
    print('Ano de alistamento: {}. Passou {} anos'.format(anoexcesso,excesso))

elif situacao == 18:
    print('Voce esta no ano do alistamento.')

elif situacao < 18:
    faltante = 18 - situacao
    anoFaltante = faltante + anohoje
    print('Ano de alistamento: {}. Ainda falta {} anos para poder se alistar'.format(anoFaltante, faltante))

