'''Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
   desconsiderando os espaços.'''

from unicodedata import normalize, category

def rem_acen(frase1):
    return ''.join(c for c in normalize('NFD', frase1)
                 if category(c) != 'Mn')

frase = input('Digite uma frase para verificar se ela é um palíndromo: ').strip()
frase_format = ''.join(rem_acen(frase).upper().split())
frase_inv = ''

for c in range(len(frase_format)-1, -1, -1):
    frase_inv += frase_format[c]

if frase_inv == frase_format:
    print(f'"{frase}" é um palíndromo')
else:
    print(f'"{frase}" não é um palíndromo')
