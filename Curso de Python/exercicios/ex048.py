"""Exercício Python 48: Faça um programa que calcule a soma entre todos
   os números que são múltiplos de três e que se encontram no intervalo de 1 até 500."""

S = 0
Q = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        M = 0
        for x in range(c+2, 500, 2):
            if x % 3 == 0:
                M = M + 1
        if M != 0:
            print('{:>3}, '.format(c), end = '')
        else:
            print('{:>3}. '.format(c), end='')
        S = S + c
        Q = Q + 1
    if Q == 25:
        print()
        Q = 0
print('\n\nA soma de todos os números ímpares múltiplos de 3 é {}'.format(S))

