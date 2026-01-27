"""Exercício Python 103: Faça um programa que tenha uma função chamada ficha(),
   que receba dois parâmetros opcionais: o nome de um jogador e quantos gols
   ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo
   que algum dado não tenha sido informado corretamente."""

def ficha(n='<desconhecido>', g=0):
    print(f'O jogador {n} fez {g} gol(s) no campeonato.')


nome = input('Nome do jogador: ')
while True:
    gols = input('Número de gols: ')
    if gols == '' or gols.isnumeric(): break
    else: print('\033[1:31mINVÁLIDO\033[m Tente novamente.', end=' ')
if nome and gols:
    ficha(nome, gols)
elif nome and not gols:
    ficha(n=nome)
elif not nome and gols:
    ficha(g=gols)
elif not nome and not gols:
    ficha()
