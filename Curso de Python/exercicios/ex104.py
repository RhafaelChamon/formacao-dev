"""Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai
  funcionar de forma semelhante ‘a função input() do Python, só que fazendo a
  validação para aceitar apenas um valor numérico.
  Ex: n = leiaInt(‘Digite um n: ‘)"""

def leiaint(msg):
    while True:
        try:
            valor = int(input(msg))
            return valor
        except (ValueError, TypeError): print('\033[1:31mERRO!\033[mDigite um inteiro válido.')


n = leiaint('Digite um número inteiro: ')
print(f'O valor digitado {n}, é inteiro.')
