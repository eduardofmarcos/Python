import datetime

nome = str(input('digite o nome: ')) .strip()
ano = int(input('Digite o ano de nascimento: '))

data = datetime.datetime.now()

anoHoje = data.year

situacao = anoHoje - ano

if situacao <= 9:
    print('Categoria Mirim')

elif situacao <= 14:
    print('Categoria Infantil')

elif situacao <= 19:
    print('Categoria Junior')

elif situacao <= 20:
    print('Categoria Senior')

else:
    print('Categoria Master')