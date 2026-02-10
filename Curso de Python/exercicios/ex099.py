"""Exercício Python 099: Faça um programa que tenha uma função chamada maior(),
   que receba vários parâmetros com valores inteiros. Seu programa tem que
   analisar todos os valores e dizer qual deles é o maior."""

from random import randint

def maior(a):
    b = 0
    for c in a:
        if int(c) > b:
            b = int(c)
    print(f'\n{"=" * 45}\n')
    print(f'Analisando os valores {", ".join(lista)}:')
    print(f'Foram {len(lista)} valores informados.')
    print(f'O maior valor informado foi {b}.')


for i in range(0, 5):
    lista = []
    k = 0
    while k < randint(1, 10):
        n = randint(1, 10)
        if str(n) not in lista:
            lista.append(str(n))
            k += 1
    maior(lista)
print(f'\n{"=" * 45}\n')
