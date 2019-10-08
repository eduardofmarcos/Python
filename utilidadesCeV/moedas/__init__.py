def metade(preco, show):
    met = preco / 2
    if show == True:
        return 'R$ ' + str(met)
    else:
        return met


def dobro(preco, show):
    dob = preco * 2
    if show == True:
        return 'R$ ' + str(dob)
    else:
        return dob


def aumentar(preco, v, show):
    d = v / 100
    au = preco + (preco*d)
    if show == True:
        return 'R$ ' + str(au)
    else:
        return au


def diminuir(preco, v, show):
    d = v /100
    di = preco - (preco*d)
    if show == True:
        return 'R$ ' + str(di)
    else:
        return di

def resumo(preco, desconto, acrescimo):
    print('**************************')
    print('**** RESUMO DO VALOR *****')
    print('**************************')
    print('')
    print('**************************')
    print('Preço analisado: R$ {}'.format(preco))
    print('Dobro do preço: {}'.format(dobro(preco, show=True)))
    print('Metade do preco: {}'.format(metade(preco, show=True)))
    print('Aumento de {}% fica {}'.format(acrescimo, aumentar(preco, acrescimo, show=True)))
    print('Diminuir {}% fica {}'.format(desconto, diminuir(preco, desconto, show=True)))
    print('')
    print('**************************')