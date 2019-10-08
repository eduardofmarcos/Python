notaUm = float(input('Digite a primeira nota: '))
notaDois = float(input('Digite a segunda nota: '))

media = (notaUm + notaDois)/2

if media < 5.0:
    print('Aluno reprovado. Sua média foi {:.2f}'.format(media))

elif media >= 5.0 and media < 7.0:
    print('Aluno em Recuperação. Sua média foi {:.2f}'.format(media))

elif media >= 7.0:
    print('Parabéns! Aluno aprovado. Sua média foi {:.2f}'.format(media))
