def leiadinheiro():
    lista = []
    while True:
        preco = (input('Digite um preco: '))
        if preco == '':
            print('Valor invalido')
        else:
            for l in preco:
                if l == ' ' or l.isalpha() or l in '@_!#$%^&*()<>?/\|}{~:]"`+=_-' or l in "'":
                    lista.append(l)
            if len(lista) == 0:
                break
            else:
                lista.clear()
                print('Valor invalido!')
    preco = float(preco.replace(',', '.'))
    return preco

















