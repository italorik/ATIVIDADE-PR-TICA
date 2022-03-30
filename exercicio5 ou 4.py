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

#Windows PowerShell
#Copyright (C) Microsoft Corporation. Todos os direitos reservados.

#Experimente a nova plataforma cruzada PowerShell https://aka.ms/pscore6

#PS C:\Users\rik\Desktop>  & 'C:\Users\rik\AppData\Local\Microsoft\WindowsApps\python3.10.exe' 'c:\Users\rik\.vscode\extensions\ms-python.python-2022.2.1924087327\pythonFiles\lib\python\debugpy\launcher' '63159' '--' 'c:\Users\rik\Desktop\exercicio4.py'
#Traceback (most recent call last):
#  File "c:\Users\rik\Desktop\exercicio4.py", line 4, in <module>
#    import requests
#ModuleNotFoundError: No module named 'requests'
#PS C:\Users\rik\Desktop> 

#Pergunta: É necessario, sempre executar em linux? if no! -Os resultados saem diferentes