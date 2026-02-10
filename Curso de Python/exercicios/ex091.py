"""Exercício Python 91: Crie um programa onde 4 jogadores joguem um dado e
   tenham resultados aleatórios. Guarde esses resultados em um dicionário em
   Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor
   tirou o maior número no dado."""

from random import randint
from time import sleep
from emoji import emojize

print(f'Os jogadores começam a rolar os dados...\n')
jog = dict()
for c in range(1, 5):
    sleep(0.5)
    jog[f'Jogador {c}'] = randint(1, 6)
    print(f'Jogador {c} tirou... {emojize(':game_die:')}', end=' ')
    sleep(1)
    print(f'{jog[f'Jogador {c}']}')
jog = sorted(jog.items(), key=lambda k: k[1], reverse=True)
sleep(0.5)

print(f'\n{' RANKING DOS VENCEDORES':=^40}\n')
for i in range(0, len(jog)):
    print(f'{i+1}ª {jog[i][0]} tirando {jog[i][1]}')
