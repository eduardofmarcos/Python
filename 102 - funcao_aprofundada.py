def leiaint():
    while True:
        try:
            numeroint = int(input('Digite um numero inteiro: '))
        except (ValueError):
            print('Numero inteiro invalido. Digite um numero inteiro')
        except (KeyboardInterrupt):
            print('\nO usuario decidiu nao inserir esse numero.')
            numeroint = 0
            return 0
        else:
            return numeroint
            break


def leiafloat():
    while True:
        try:
            numeroflo = float(input('Digite um numero real: '))
        except (ValueError):
            print('Numero real invalido. Digite um valor real valido.')
        except (KeyboardInterrupt):
            print('O usuario decidiu nao inserir esse numero.')
            numeroflo = 0
            return 0
        else:
            return numeroflo
            break


print('o numero inteiro é {} e o real é {}'.format(leiaint(), leiafloat()))
