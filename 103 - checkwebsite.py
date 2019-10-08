import urllib.request
try:
    v = urllib.request.urlopen("http://www.pudim.com.br").getcode()
except (urllib.error.URLError):
    print('O site está fora ou sua conexão não esta disponivel no momento.')
else:
    print('O site esta no ar!')
