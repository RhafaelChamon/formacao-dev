"""Exercício Python 28: Escreva um programa que faça o computador “pensar” em um
   número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o
   número escolhido pelo computador. O programa deverá escrever na tela se o
   usuário venceu ou perdeu."""

from random import randint
numjog = int(input('Adivinhe o número inteiro entre 1 e 5: '))
numbot = randint(1, 5)
if numjog == numbot:
    print('Parabéns, Você venceu o jogo! {} era o número escolhido!'.format(numjog))
else:
    print('Mais sorte da próxima vez! {} era o número escolhido.'.format(numbot))
