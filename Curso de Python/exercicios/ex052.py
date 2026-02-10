"""Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo."""

print('-'*27)
print(f'|{'Verificador de Primos':^25}|')
print('-'*27)
n = int(input('Digite um número inteiro, para verificar se ele é primo: '))
div = 0

for c in range(n, 0, -1):
    if n % c == 0:
        div += 1
if div == 2:
    print(f'{n} é primo')
else:
    print(f'{n} não é primo')
