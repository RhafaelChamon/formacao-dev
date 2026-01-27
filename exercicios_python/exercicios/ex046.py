"""Exercício Python 46: Faça um programa que mostre na tela uma contagem regressiva para o
   estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles."""

from time import sleep
from emoji import emojize

print('{} Contagem regressiva para os fogos {} {}'.format('='*10, emojize(':fireworks:'), '='*10))
for c in range(10, 0, -1):
    print('{}...'.format(c), end = '')
    sleep(1)
print('\n', end = '')
print(emojize(':fireworks:'*20))
