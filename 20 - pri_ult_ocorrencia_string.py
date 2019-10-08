frase = str(input('Digite uma frase: ')).upper().strip()


n = frase.count('A')
primea = frase.find('A')
ultimoa = frase.rfind('A')

print('"a" aparece {} vezes'.format(n))
print('O primeiro "a" aparece na posição {}'.format(primea))
print('O ultimo "a aparece na posição {}'.format(ultimoa))

