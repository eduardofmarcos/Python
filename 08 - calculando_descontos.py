#ex0012>>> Leia o preço de um produto e de o valor de desconto.

preco = float(input('Digite o preco de um produto: '))
desc = int(input('Digite o desconto em %: '))

por = desc/100

print('O valor do produto é de {:.2f} e aplicado o desconto de {}% ele fica por {:.2f}'.format(preco, desc, preco-preco*por))


