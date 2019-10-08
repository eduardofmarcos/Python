palavras = ('mercado', 'futuro', 'programa', 'peso', 'palio', 'mar', 'sol', 'prancha',)
for count in range(0,len(palavras)):
    print('\n',palavras[count],end=' -> ')
    for index in range(len(palavras[count])):
       if palavras[count][index] == 'a':
           print(palavras[count][index], end=' ')
       elif palavras[count][index] == 'e':
           print(palavras[count][index], end=' ')
       elif palavras[count][index] == 'i':
           print(palavras[count][index], end=' ')
       elif palavras[count][index] == 'o':
           print(palavras[count][index], end=' ')
       elif palavras[count][index] == 'u':
           print(palavras[count][index], end=' ')
