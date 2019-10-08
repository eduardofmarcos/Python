import datetime
dados = dict()
dados['nome'] = str(input('Digite o nome: '))
dados['ano'] = int(input('Digite o ano de nascimento: '))
dados['cart'] = int(input('Numero da carteira de trabalho. (0 para nao possui CTPS): '))
dados['idade'] = datetime.datetime.today().year - dados['ano']
if dados['cart'] == 0:
    print('Nome: {}'.format(dados['nome']))
    print('Idade: {}'.format(dados['idade']))
if dados['cart'] != 0:
    dados['anocontrat'] = int(input('Digite o ano de contratação: '))
    dados['salario'] = float(input('Digite o salario: '))
    dados['idadeapos'] = (35 - (datetime.datetime.today().year - dados['anocontrat'])) + dados['idade']
    print('Nome: {}'. format(dados['nome']))
    print('Idade: {}'.format(dados['idade']))
    print('Idade da aposentadoria: {}'.format(dados['idadeapos']))