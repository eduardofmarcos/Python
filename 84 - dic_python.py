aluno = dict()
aluno['Nome'] = input('Digite o nome: ')
aluno['Media'] = int(input('Digite a media: '))
if aluno['Media'] >= 7:
    aluno['Situacao'] = 'Aprovado'
else:
    aluno['Situacao'] = 'Reprovado'
print(aluno)

for k, v in aluno.items():
    print('{} é igual a {}'.format(k, v))
