"""Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela
   os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
   0 – 1 – 1 – 2 – 3 – 5 – 8 """

print('-=-'*20)
print(f'|{'Sequência de Fibonacci':^58}|')
print('-=-'*20)

N = int(input('Quantos elementos da Sequência de Fibonacci você gostaria de ver? '))
if N == 0:
    n1 = 0
    n2 = 1
    print('')
elif N == 1:
    n1 = 0
    n2 = 1
    print(f'{n1}')
elif N == 2:
    n1 = 0
    n2 = 1
    print(f'{n1}, {n2}')
elif N >= 3:
    n1 = 0
    n2 = 1
    print(f'{n1}, {n2}, ', end = '')
    c = 3
    while c <= N:
        n3 = n1 + n2
        print(f'{n3}, ' if c < N else f'{n3}', end = '')
        n1 = n2
        n2 = n3
        c += 1
