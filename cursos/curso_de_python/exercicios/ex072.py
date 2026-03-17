"""Exercício Python 72: Crie um programa que tenha uma dupla totalmente
   preenchida com uma contagem por extenso, de zero até vinte. Seu programa
   deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso."""

while True:
    extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
               'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
               'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

    while True:
        try:
            num = int(input('Digite um número entre 0 e 20: '))
            if num >= 0 and num <= 20:
                print(f'Você digitou o número {extenso[num]}.')
                break
            else:
                print('Tente novamente!', end=' ')
        except ValueError:
            print('Tente novamente!', end=' ')
    while True:
        continuar = input('Deseja continuar? [S/N] ').strip().upper()
        if bool(continuar) == True and continuar[0] in 'SN':
            break
        else:
            print('Tente novamente!', end=' ')
    if continuar == 'N':
        break
