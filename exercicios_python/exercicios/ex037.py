"""Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer
   e peça para o usuário escolher qual será a base de conversão:
   1 para binário, 2 para octal e 3 para hexadecimal."""

num = int(input('Digite um numero inteiro: '))
print ('Gostaria de converter {} para qual sistema de numeração?\n'
       '[1] Binário\n'
       '[2] Octal\n'
       '[3] Hexadecimal'.format(num))
op = int(input('Opção escolhida: '))
if op == 1:
    print('{} em binário é {}'.format(num, bin(num)[2:]))
elif op == 2:
    print('{} em octal é {}'.format(num, oct(num)[2:]))
elif op == 3:
    print('{} em hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('Opção não encontrada!')
