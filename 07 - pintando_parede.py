#ex011>>> Faça um program que leia a altura e largura de uma parece em metros, calcule a area e a
#quantidade de tinta para pinta-la. Sabendo que cada litro de tinta pinta 2m2.

largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))
area = largura*altura

print('A area da parede é: {:.2f} m2 e quantidade de tinta necessaria para a pintura é de {:.2f} litros'.format(area, area/2))

