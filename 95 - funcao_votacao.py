def voto(ano):
    """
    :param ano: Ano de nascimento
    :return: idade, posição de voto.
    """
    import datetime
    idade = datetime.datetime.today().year - ano
    if idade < 16:
        v = 'Você tem {} anos. Voto negado.'.format(idade)
        return v

    if idade >= 16 and idade < 18:
        v = 'Você tem {} anos. Voto opcional.'.format(idade)
        return v
    if idade >= 18 and idade <= 65:
        v = 'Você tem {} anos. Voto Obrigatorio.'.format(idade)
        return v
    if idade > 65:
        v = 'Você tem {} anos. Voto Opcional.'.format(idade)
        return v


#programa principal
ano = int(input('Digite o ano de seu nascimento: '))
print(voto(ano))



