precoProduto = float(input('Digite o preço do produto: '))
print('-'*50)
print('Digite a forma de pagamento:\n'
                            '1 - a vista/ cheque: \n'
                            '2 - a vista no cartão: \n'
                            '3 - 2x no cartão: \n'
                            '4 - 3x ou mais no cartao: ')

print('-'*50)
formaPagamento = int(input('Digite a forma de pagamento: '))

if formaPagamento == 1:
    precoFinal = precoProduto - (precoProduto * 0.10)
    print('O valor do seu produto é: {:.2f}'.format(precoFinal))

elif formaPagamento == 2:
    precoFinal = precoProduto - (precoProduto * 0.05)
    print('O valor do seu produto é: {:.2f}'.format(precoFinal))

elif formaPagamento == 3:
    print('O valor do seu produto é: {:.2f}'.format(precoProduto))

elif formaPagamento == 4:
    precoFinal = precoProduto + (precoProduto * 0.2)
    print('O valor do seu produto é: {:.2f}'.format(precoFinal))

else:
    print('Digite um valor entre 1 e 4.')
