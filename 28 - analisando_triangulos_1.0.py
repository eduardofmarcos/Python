print('-='*20)
print('Analisador de triangulos')
print('-='*20)

a = float(input('Digite a primeira medida: '))
b = float(input('Digite a segunda medida: '))
c = float(input('Digite a terceira medida: '))

if (a+b) > c and (a+c) > b and (b+c) > a:
    print('Temos um triangulo')

else:
    print('Não temos um triangulo')




