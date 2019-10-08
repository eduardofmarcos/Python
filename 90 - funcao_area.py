print('Medidor de terrenos')
print('=-'*20)

def area(largura, comprimento):
    area = largura * comprimento
    print('A area do terreno é {}m²'.format(area))


while True:
    largura = float(input('Digite a largura do terreno: '))
    comprimento = float(input('Digite o comprimento do terreno: '))
    area(largura, comprimento)
    opt = input('Deseja continuar?')
    if opt in 'Nn':
        break