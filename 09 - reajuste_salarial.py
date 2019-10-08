#ex013>>> Digite um salario e mostre o salario acrecido de 15% de aumento

sal = float(input('Digite seu salario atual: '))
acres = int(input('Digite o aumento em %: '))

por = acres/100

print('Seu salario era {:.2f} e com o acrescimo de {}% passou a ficar {:.2f}'.format(sal, acres, sal+(sal*por)))
