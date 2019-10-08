from math import sin, tan, cos, radians

ang = float(input('Digite um angulo qualquer: '))

seno = sin(radians(ang))
tangente = tan(radians(ang))
coseno = cos(radians(ang))

print('Segue seno: {:.3f}, coseno: {:.3f} e tangente: {:.3f} do angulo informado: '.format(seno, coseno, tangente))

