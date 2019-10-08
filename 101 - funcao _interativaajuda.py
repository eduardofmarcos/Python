def doc(com=input('Digite a funcao: ').lower()):
    while com != "fim":
        print('')
        t = len(com)
        total = t + 31
        print('*' * total)
        print('Acessando manual do comando "{}":'. format(com))
        print('*' * total)
        print('')
        help(com)
        print('*' * 16)
        com = str(input('Digite a funcao: ')).lower()
        print('*' * 16)
    print('Obrigado!')


#Programa Principal
doc()
