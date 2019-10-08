palavras = ('mercado', 'futuro', 'programa', 'peso', 'palio', 'mar', 'sol', 'prancha',)
for count in range(0,len(palavras)):
    print('\n', palavras[count], end=' -> ')
    for index in range(len(palavras[count])):
       if palavras[count][index] in 'aeiou':
           print(palavras[count][index], end=' ')
