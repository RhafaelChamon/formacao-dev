"""Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre
   na tela cada um dos dígitos separados."""

num = int(input('Digite um número inteiro de 0 a 9999: '))
print('Analisando o número {}'.format(num))
if num >= 0 and num <= 9999:
    num = str(num).strip()
    n = len(num)

    n = len(str(num).strip())

    if n >= 1 and n <= 4:
        print('Unidade: {}'.format(num[n-1]))
    else:
        print('Unidade: N/A')

    if n >= 2 and n <= 4:
        print('Dezenas: {}'.format(num[n-2]))
    else:
        print('Dezenas: N/A')

    if n >= 3 and n <= 4:
        print('Centenas: {}'.format(num[n-3]))
    else:
        print('Centenas: N/A')

    if n == 4:
        print('Milhar: {}'.format(num[n-4]))
    else:
        print('Milhar: N/A')
else:
    print('{} não é válido'.format(num))
