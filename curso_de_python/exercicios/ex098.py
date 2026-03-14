"""Exercício Python 098: Faça um programa que tenha uma função chamada contador(),
   que receba três parâmetros: início, fim e passo. Seu programa tem que realizar
   três contagens através da função criada:
   a) de 1 até 10, de 1 em 1
   b) de 10 até 0, de 2 em 2
   c) uma contagem personalizada"""

from time import sleep

def contador(a, b, x):
    k = b
    if a < b:
        b += 1
        if x < 0: x *= -1
        elif x == 0: x = 1
    elif a > b:
        b -= 1
        if x > 0: x *= -1
        elif x == 0: x = -1
    elif a == b:
        b += 1
        if x != 1: x = 1
    print(f'Contagem de {a} a {k} de {abs(x)} em {abs(x)}')
    for c in range(a, b, x):
        print(c, end=' ')
        sleep(0.2)
    print('\n')


def duple_line():
    print(f'{"=" * 40}\n')


duple_line()
contador(1, 10, 1)
duple_line()
contador(10, 0, -2)
print(f'{" CONTAGEM PERSONALIZADA ":=^40}')
print('Agora faça uma contagem personalizada!')
while True:
    try: i = int(input('Inicio: ')); break
    except ValueError: print('\033[1:31mINVÁLIDO!\033[m Tente novamente.', end=' ')
while True:
    try: f = int(input('Fim: ')); break
    except ValueError: print('\033[1:31mINVÁLIDO!\033[m Tente novamente.', end=' ')
while True:
    try: p = int(input('Passo: ')); break
    except ValueError: print('\033[1:31mINVÁLIDO!\033[m Tente novamente.', end=' ')
contador(i,f, p)
