"""Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.
   No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores."""

from datetime import datetime

ano_atual = datetime.now().year
maior = 0
not_maior = 0
for c in range(1, 8):
    nasc = int(input(f'Qual o ano de nascimento da {c}º pessoa? '))
    idade = ano_atual - nasc
    if idade < 18:
        not_maior += 1
    else:
        maior += 1
print(f'{maior} pessoas atingiram a maioridade, e {not_maior} não atingiram.')
