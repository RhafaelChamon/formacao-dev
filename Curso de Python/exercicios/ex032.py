"""Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto."""

ano = int(input('Digite um ano para verifica-lo se ele é bissexto ou não: '))
bis = ano % 4
if bis == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é bissexto.'.format(ano))
else:
    print('{} não é bissexto.'.format(ano))
