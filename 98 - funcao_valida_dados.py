def leiaint(string=input('Digite um numero: ')):
    if string.isnumeric() == True:
        return string
    else:
        while string.isnumeric() == False:
            string = input('Digite um numero: ')
            if string.isnumeric():
                return string
                break
n = leiaint()
print('voce digitou {}'.format(n))










