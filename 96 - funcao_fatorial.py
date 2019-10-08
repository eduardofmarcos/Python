def fatorial(inicio, show=0):
    '''

    :param inicio: Numero do fatorial desejado
    :param show: Se True, mostra o calculo do fatorial
    :return: i = resultado do fatorial
    '''
    p = 1
    c = inicio
    if show == True:
        for i in range(1, inicio+1):
            p = p * i
            i = p
            c = c - 1
            print(c+1,end=' x ')
        return i
    else:
        for i in range(1, inicio + 1):
            p = p * i
            i = p
        return i
inicio = int(input('Deseja o fatorial de que numero? '))
print(fatorial(inicio))
opcao = str(input('Deseja ver o calculo: [S] Sim // [N]: ')).upper()[0]
if opcao == 'S':
    print(' = ', fatorial(inicio, True))
