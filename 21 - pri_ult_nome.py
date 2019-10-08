nome = str(input('Digite seu nome: ')).upper()

divisao = nome.split()

primeiro = divisao.index(min(divisao))
ultimo = divisao.index(max(divisao))

primeironome = divisao[primeiro]
ultimonome = divisao[ultimo]

print('O primeiro nome é: {}'.format(primeironome))
print('O ultimpo nome é: {}'.format(ultimonome))



