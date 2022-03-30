#viacep.com.br/ws/MG/Belo Horizonte/Rua dos Aimores/json/

from turtle import goto
from urllib import request
import requests

x = resquests.get('https://viacep.com.br/ws/')
rua =('Rua dos Aimores/json/')
formato = '/json/'
# tem um erro na comparação da rua que não entendi/ deveria comparar com rua ==?????
request
print(x.headers)
print(x.headers['Server'])
print(X.status_code)

if x.status_code == 200:
    print("Connectado")
elif x.status_code == 404:
    print("Não encontrado")
    
lista = ['Rua dos Aimorés, 66 - Funcionários, Belo Horizonte - MG, 30140-920, Rua dos Aimorés, de 2371/2372 a 2759/2760 - Santo Agostinho, Belo Horizonte - MG, 30140-076, Rua dos Aimorés, de 2761/2762 a 3299/3300 - Barro Preto, Belo Horizonte - MG, 30140-073, Rua dos Aimorés, de 531/532 a 969/970 - Funcionários, Belo Horizonte - MG, 30140-075, Rua dos Aimorés, de 971/972 a 1399/1400 - Boa Viagem, Belo Horizonte - MG, 30140-071, Rua dos Aimorés, de 3301/3302 ao fim - Barro Preto, Belo Horizonte - MG, 30140-078, Rua dos Aimorés, de 1401/1402 a 1799/1800 - Lourdes, Belo Horizonte - MG, 30140-07]    

while rua == lista:
    print (x.)
    print(x.headers)
    print(x.headers['Server'])
    print(X.status_code)
goto :request
exit()