print('-='*20)
print('Analisador de triangulos')
print('-='*20)

a = float(input('Digite a primeira medida: '))
b = float(input('Digite a segunda medida: '))
c = float(input('Digite a terceira medida: '))



if (a+b) > c and (a+c) > b and (b+c) > a:

    if (a + b) == (a + c):
        if (a + c) == (b + c):
            print('Temos um triangulo Equilátero')

    if (a + b) == (a + c) and (a + b) != (b + c):
        print('Temos um triangulo Isóceles')
    elif (a + b) == (b + c) and (a + b) != (a + c):
        print('Temos um triangulo Isóceles')
    elif (b + c) == (a + c) and (a + c) != (a + b):
        print('Temos um triangulo Isóceles')

    if (a + b) != (b + c) and (a + b) != (a + c) and (a + c ) != (b + c):
        print('Temos um triangulo Escaleno')



else:
    print('Não temos um triangulo')