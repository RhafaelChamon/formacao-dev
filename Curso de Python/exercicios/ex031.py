"""Exercício Python 31: Desenvolva um programa que pergunte a distância
   de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50
   por Km para viagens de até 200Km e R$0,45 parta viagens mais longas."""

from re import findall

dis = input('Qual a distância da viagem? ')

dform = findall(r'\d+', dis)
if dform:
    dform = int(dform[0])
    if dform <= 200:
        print('O preço da passagem é R$0.50 x {}Km = R${:.2f}'.format(dform, dform * 0.50))
    else:
        print('O preço da passagem é R$0.45 x {}Km = R${:.2f}'.format(dform, dform * 0.45))
else:
    print('Cancelado...')
