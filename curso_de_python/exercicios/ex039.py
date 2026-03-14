"""Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe,
   de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora
   exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá
   mostrar o tempo que falta ou que passou do prazo."""

import datetime

anoatual = int(datetime.datetime.now().year)
anonasc = int(input('Em qual ano você nasceu: '))
idade = (anoatual - anonasc)

print('\nComo você nasceu em {} você tem em {}, {} anos'.format(anonasc, anoatual, idade))
if idade < 18:
    print('Ainda faltam {} anos para você poder se alistar.'.format(18 - idade))
elif idade == 18:
    print('Você tem {} anos e já pode se alistar.'.format(idade))
else:
    print('Já passou {} anos do tempo de você de alistar.'.format(idade - 18))
