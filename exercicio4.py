#4) Modifique o primeiro código de tal forma que o endereço " https://viacep.com.br/abc/"
#tente ser acessado. Exiba o código de retorno e o texto.

import requests

x = resquests.get('https://viacep.com.br/abc/')
cep = '30140071'
formato = '/json/'

print(x.headers)
print(x.headers['Server'])
print(X.status_code)

if x.status_code == 200:
    print("Connectado")
elif x.status_code == 404:
    print("Não encontrado")

print(x.enlapsed)
print(x.cookies)

x = requests.get('https://viacep.com.br/ws/')
print(x.url)