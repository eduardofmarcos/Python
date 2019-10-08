boletim = []
alunos = []
notas = []
t = 0
while True:
    nome = str(input('Digite o nome do aluno: ')).strip().upper()
    n1 = float(input('Digite a nota 1 do aluno: '))
    n2 = float(input('Digite a nota 2 do aluno: '))
    media = (n1+n2) / 2
    alunos.append(nome)
    alunos.append(media)
    notas.append(n1)
    notas.append(n2)
    alunos.append(notas[:])
    notas.clear()
    boletim.append(alunos[:])
    alunos.clear()
    opt = str(input('Deseja continuar: ')).strip().upper()
    if opt in 'N':
        break

print('*'*40)
print('')
for dados in boletim:
    t = t+1
    for i in range(0, 1):
        print('{} - {} - média - {:.2}'.format(t-1, dados[0], dados[1]))
print('')
print('*'*40)
print('')
while True:
    p = int(input('Deseja mostrar as notas de que aluno? [888] para sair: '))
    if p == 888:
        break
    else:
        print('As notas de {} é {}'.format(boletim[p][0], boletim[p][2]))
print('Obrigado!')