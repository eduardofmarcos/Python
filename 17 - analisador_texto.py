nome = input('Digite o nome de uma pessoa: ').strip()

n = nome.count(' ')
novonome = len(nome) - n

primeironome = nome.split()

print(nome.upper())
print(nome.lower())
print(len(nome))
print(novonome)
print('O primeiro nome é {} e tem {} letras'.format(primeironome[0], len(primeironome[0])))

