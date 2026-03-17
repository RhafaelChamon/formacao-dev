"""Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
   Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram
   necessários para vencer."""

from random import randint
from time import sleep

print(f'{'\033[:36m-='*20}-\033[m')
print(f'\033[:36m|\033[m{'Jogo da Adivinhação':^39}\033[:36m|\033[m')
print(f'{'\033[:36m-='*20}-\033[m')

print('Vou pensar em um número inteiro qualquer entre \033[1:31m1 e 10\033[m, e você irá tentar adivinhá-lo...')
sleep(2)
print('Vamos começar...')
sleep(1)
print('\033[:37mPensando...\033[m')
bot = randint(1, 10)
sleep(4)
print('\nÓtimo! Já escolhi, e agora tente adivinhar o número que escolhi.')
erros = 0
jog = 0
while jog != bot:
    jog = int(input('Qual é o número? '))
    if jog == bot:
        if erros == 0:
            print(f'Parabéns, você acertou! {bot} era o número que escolhi! E você errou nenhuma vez!')
        elif erros == 1:
            print(f'Parabéns, você acertou! {bot} era o número que escolhi! E você errou 1 vez!')
        else:
            print(f'Parabéns, você acertou! {bot} era o número que escolhi! E você errou {erros} vezes!')
    else:
        erros += 1
        print(f'{jog} não era o número que escolhi... Tente novamente!')
