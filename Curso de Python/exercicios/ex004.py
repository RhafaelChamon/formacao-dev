"""Exercício Python 4: Faça um programa que leia algo pelo teclado e mostre
   na tela o seu tipo primitivo e todas as informações possíveis sobre ele."""

x = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(x))
print('Só tem espaço? ', x.isspace())
print('É um número? ', x.isnumeric())
print('É alfabético? ', x.isalpha())
print('É alfanumérico? ', x.isalnum())
print('Está em maiúsculas? ', x.isupper())
print('Está em minúsculas? ', x.islower())
print('Está capitalizada (formato de título)? ', x.istitle())
