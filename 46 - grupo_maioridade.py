import datetime

ano = datetime.datetime.now().year
numeroCadastro = int(input('Digite quantas pessoas voce quer cadastrar: '))
menor = 0
maior = 0

for contador in range(0, numeroCadastro):
    nome = str(input('Digite seu nome: '))
    dataNascimento = int(input('Digite sua data de nascimento: '))
    classificacao = ano - dataNascimento

    if classificacao <= 18:
        menor = menor + 1


    if classificacao > 18:
        maior = maior + 1


print('Temos {} usuarios cadastrados maior de idade'.format(maior))
print('Temos {} usuarios cadastrados menor de idade'.format(menor))


