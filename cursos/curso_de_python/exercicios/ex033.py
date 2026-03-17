"""Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor."""

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo: '))
n3 = int(input('Digite o terceiro: '))

if n1 < n2:
    aux = n1
    n1 = n2
    n2 = aux

if n1 < n3:
    aux = n1
    n1 = n3
    n3 = aux

if n2 < n3:
    aux = n2
    n2 = n3
    n3 = aux

print('O maior número é {} e o menor é {}'.format(n1, n3))
