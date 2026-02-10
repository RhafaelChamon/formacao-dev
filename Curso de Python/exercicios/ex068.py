"""Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
   O jogo só será interrompido quando o jogador perder, mostrando o total de
   vitórias consecutivas que ele conquistou no final do jogo."""

from random import randint
print('=-'*15)
print(f'{'VAMOS JOGAR PAR OU ÍMPAR':^30}')
vit = 0
while True:
    print('=-' * 15)
    jog = int(input('Diga um valor: '))
    PI = input('Par ou Ímpar? [P/I] ').strip().upper()[0]
    print('-'*30)
    bot = randint(1, 10)
    s = jog + bot
    if s % 2 == 0:
        print(f'Você jogou {jog} e o computador {bot}. Total de {s} DEU PAR')
    else:
        print(f'Você jogou {jog} e o computador {bot}. Total de {s} DEU ÍMPAR')
    print('-' * 30)
    if PI == 'P':
        if s % 2 == 0:
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            vit += 1
        else:
            print('Você PERDEU!')
            break
    elif PI in 'IÍ':
        if s % 2 == 1:
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            vit += 1
        else:
            print('Você PERDEU!')
            break
print('=-' * 15)
print(f'GAMER OVER! Você venceu {vit} vezes.')
