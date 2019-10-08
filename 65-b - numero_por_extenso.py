extenso = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quartorze','quinze','desseseis','dezessete','dezoito','dezenove','vinte')
while True:
    numero = int(input('Digite um numero entre 0 e 20: '))
    if numero < 0 or numero > 20:
        True
    else:
        print('O numero digitado por extenso é: {}'.format(extenso[numero]))
        break