from turtle import goto
from urllib import request
import requests

x = resquests.get('https://viacep.com.br/ws/')
cep = '30140071'
formato = '/json/'

request
print(x.headers)
print(x.headers['Server'])
print(X.status_code)

if x.status_code == 200:
    print("Connectado")
elif x.status_code == 404:
    print("Não encontrado")
    
lista = [30140071, 30140072, 30140073, 30140074, 30140075]    
while cep == lista:
    print (x.cep)
    print(x.headers)
    print(x.headers['Server'])
    print(X.status_code)
goto :request

print(x.enlapsed)
print(x.cookies)

x = requests.get('https://viacep.com.br/ws/')
print(x.url)