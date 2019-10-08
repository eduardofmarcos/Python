def risco(msg):
    t = len(msg)
    print('*'*t)
    print('{:2}'.format(msg))
    print('*'*t)


msg = str(input('Digite uma mensagem: ')).strip()

risco(msg)