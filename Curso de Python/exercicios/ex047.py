"""Exercício Python 47: Crie um programa que mostre na tela todos os
   números pares que estão no intervalo entre 1 e 50."""

print('2', end = '')
for c in range(3, 51):
    if c % 2 == 0:
        print(', {}'.format(c), end = '')
