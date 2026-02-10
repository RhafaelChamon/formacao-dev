"""Exercício Python 14: Escreva um programa que converta uma temperatura
   digitando em graus Celsius e converta para graus Fahrenheit."""

C = float(input('Informe a temperatura em ºC: '))
F = C * 1.8 + 32
print('A temperatura de {:.1f}ºC correspondem a {:.1f}ºF.'.format(C, F))
