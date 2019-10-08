nomeLista = []
idadeLista = []
sexoLista = []
masculinaLista = []
masculinaIdade = []
femininaIdade = 0

for contador in range(0, 4):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo: '))

    nomeLista.append(nome)
    idadeLista.append(idade)
    sexoLista.append(sexo)

    if sexo == 'masculino':
        masculinaLista.append(nome)
        masculinaIdade.append(idade)

    if sexo == 'feminino' and idade < 18:
        femininaIdade = femininaIdade + 1

    print('=-'*50)


maxidade = masculinaIdade.index(max(masculinaIdade))
homemVelho = masculinaLista[maxidade]
print('O homem mais velho é {}' .format(homemVelho))

print('Existe {} mulheres abaixo de 18 anos'.format(femininaIdade))

mediaIdade = sum(idadeLista) / 4
print('A media da idade do grupo é de {} anos'.format(mediaIdade))

