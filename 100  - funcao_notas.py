def notas(*num, show=True):
    '''

    :param num: args
    :param show: opção para verificar situação
    :return: menor, maior, soma, media, quantidade
    '''
    soma = 0
    c = 0
    no = []
    for i in num:
        soma = soma + i
        c = c + 1
        no.append(i)
    media = soma / c
    maior = max(no)
    menor = min(no)
    dados = {'soma': soma, 'media': media, 'maior': maior, 'menor': menor, 'quantidade': c}
    if show == True:
        if media >= 7:
            situacao = 'Aprovado'
            dados = {'soma': soma, 'media': media, 'maior': maior, 'menor': menor, 'quantidade': c, 'situação': situacao}
            return dados
        elif media < 7:
            situacao = 'Reprovado'
            dados = {'soma': soma, 'media': media, 'maior': maior, 'menor': menor, 'quantidade': c, 'situação': situacao}
            return dados
    else:
        return dados


#programa principal
resp = notas(8, 8, 8, 8, show=True)
print(resp)
help(notas)
