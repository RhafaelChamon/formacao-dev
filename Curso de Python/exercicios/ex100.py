"""Exercício Python 100: Faça um programa que tenha uma lista chamada números e
   duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5
   números e vai colocá-los dentro da lista e a segunda função vai mostrar a
   soma entre todos os valores pares sorteados pela função anterior."""

from random import randint

def sorteia(a):
    print(f'Os valores sorteados foram:', end=' ')
    for c in range(0,5):
        n = randint(1,10)
        if c == 0: print(f'{n}', end='')
        else: print(f', {n}', end='')
        a.append(n)
    print()


def somapar(a):
    s = 0
    for k in a:
        if k % 2 == 0:
            s += k
    print(f'A soma de todos os valores pares é {s}')


numeros = list()
sorteia(numeros)
somapar(numeros)
