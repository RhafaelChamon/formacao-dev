"""Exercício Python 88: Faça um programa que ajude um jogador da MEGA SENA a
   criar palpites.O programa vai perguntar quantos jogos serão gerados e vai
   sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma
   lista composta."""

from random import randint
from time import sleep

print(f'{" BILHETES MEGA SENA ":=^40}')
while True:
    try: n = int(input('Quantos jogos você quer sortear ? ')); break
    except ValueError: print('\033[1:31mERRO!\033[m Tente novamente!')

jogos = []
for i in range(1, n+1):
    bilhete = []
    for k in range(1, 7):
        while True:
            j = randint(1, 60)
            if j not in bilhete: bilhete.append(j); break
    jogos.append(sorted(bilhete.copy()))

print(f'{" JOGOS SORTEADOS ":=^40}\n')
for i in range(0, n):
    sleep(1)
    print(f'Jogo {i+1}: {jogos[i]}')
print(f'\n{" \033[1:32mBOA SORTE!\033[m ":=^40}')
