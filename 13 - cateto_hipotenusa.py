from math import hypot

catadj = float(input('Digite o cateto adjacente: '))
catop = float(input('Digite o cateto oposto: '))

hyp = hypot(catadj,catop)

print('A hipotenusa é: {:.3f}'.format(hyp))

