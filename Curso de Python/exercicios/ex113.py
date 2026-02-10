"""Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio
   104, incluindo agora a possibilidade da digitação de um número de tipo
   inválido. Aproveite e crie também uma função leiaFloat() com a mesma
   funcionalidade."""

def leiaint(msg):
    while True:
        try:
            valor = int(input(msg))
            return valor
        except (ValueError, TypeError) as erro:
            print(f'\033[1:31mERRO: {erro.__class__}.\033[m Digite um número inteiro valido.')
        except KeyboardInterrupt as erro:
            print(f'\n\033[1:31mERRO: {erro.__class__}.\033[m Usuário não digitou o valor')
            return 0


def leiafloat(msg):
    while True:
        try:
            valor = float(input(msg))
            return valor
        except (ValueError, TypeError) as erro:
            print(f'\033[1:31mERRO: {erro.__class__}.\033[m Digite um número inteiro valido.')
        except KeyboardInterrupt as erro:
            print(f'\n\033[1:31mERRO: {erro.__class__}.\033[m Usuário não digitou o valor')
            return 0


n1 = leiaint('Digite um valor inteiro: ')
n2 = leiafloat('Digite um valor decimal: ')
print(f'O valor inteiro digitado foi {n1} e o decimal foi {n2}')
