nome = str(input('Digite seu nome: ')).strip()
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))

imc = peso / (altura*altura)

print('Seu IMC é: {:.2f}'.format(imc))

if imc < 18.5:
    print('Você está abaixo do peso')

elif imc >= 18.5 and imc < 25:
    print('Você está no peso ideal')

elif imc >= 25 and imc < 30:
    print('Você esta com sobrepeso')

elif imc >= 30 and imc < 40:
    print('Você esta obeso')

elif imc >= 40:
    print('Você esta com obesidade morbida')

