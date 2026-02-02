import requests

try:
    r = requests.get('https://pudim.com.br/')
    if r.status_code == 200:
        print(f'\033[32mO site Pudim esta disponível!\033[m Status code: {r.status_code}')
    else:
        print(f'\033[31mO site Pudim esta indisponível!\033[m Status code: {r.status_code}')
except Exception as erro:
    print(f'\033[31mNão consegui acessar o site Pudim!\033[m Erro: {erro.__class__}')
