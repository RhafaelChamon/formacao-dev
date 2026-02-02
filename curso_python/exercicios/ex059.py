"""Exercício Python 59: Crie um programa que leia dois valores e mostre um menu na tela:
       [ 1 ] somar
       [ 2 ] multiplicar
       [ 3 ] maior
       [ 4 ] novos dados
       [ 5 ] sair do programa
   Seu programa deverá realizar a operação solicitada em cada caso. """

from time import sleep

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

if n1 % 1 == 0:
    n1 = int(n1)
if n2 % 1 == 0:
    n2 = int(n2)

op = 0
while op != 5:
    print('\nEscolha qual das opções abaixo, você gostaria de realizar:\n'
            f'   [ 1 ] Somar {n1} e {n2}\n'
            f'   [ 2 ] Multiplicar {n1} por {n2}\n'
            f'   [ 3 ] Analiar qual é o maior entre {n1} e {n2}\n'
            f'   [ 4 ] Digitar novos valores\n'
            f'   [ 5 ] Sair do programa')
    op = int(input('Opção escolhida: '))

    if op == 1:
        soma = n1 + n2
        print(f'\033[1mA soma entre {n1} e {n2} é {soma}\033[m')
    elif op == 2:
        mult = n1 * n2
        print(f'\033[1mO produto de {n1} e {n2} é {mult}\033[m')
    elif op == 3:
        if n1 > n2:
            print(f'\033[1mO maior entre {n1} e {n2} é {n1}\033[m')
        elif n1 < n2:
            print(f'\033[1mO maior entre {n1} e {n2} é {n2}\033[m')
        else:
            print(f'\033[1m{n1} e {n2} são iguais\033[m')
    elif op == 4:
        n1 = float(input('Digite um novo valor para o primeiro número: '))
        n2 = float(input('Digite outro novo valor para o segundo número: '))
        if n1 % 1 == 0:
            n1 = int(n1)
        if n2 % 1 == 0:
            n2 = int(n2)
    elif op == 5:
        print('\033[1mSaindo do programa...\033[m')
        sleep(2)
    else:
        print('\033[1mOpção inválida. Tente novamente.\033[m')
