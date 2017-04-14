import requests

texto = None
try:
    requisicao = requests.get('http://g1.com.br')
    texto = requisicao.text
except Exception as e:
    print('A requisicao deu Erro!')

print(texto)