import requests
r = requests.get('http://www.google.com/search', params={'q':
'Protocolo HTTP'})
if (r.status_code == 200):
print()
print('Retorno : ', r.text)
print()
else:
print('Nao houve sucesso na requisicao.')

#algo de errado não esta certo! isto nao roda sem importação do linux