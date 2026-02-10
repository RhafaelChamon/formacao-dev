"""Exercício Python 55: Faça um programa que leia o peso de cinco pessoas.
   No final, mostre qual foi o maior e o menor peso lidos. """

peso = float(input('Qual o peso da 1º pessoa (Kg)? '))
maior_peso = peso
menor_peso = peso
for c in range(2, 6):
    peso = float(input(f'Qual o peso da {c}º pessoa (Kg)? '))
    if peso > maior_peso:
        maior_peso = peso
    if peso < menor_peso:
        menor_peso = peso

if maior_peso % 1 == 0 and menor_peso % 1 == 0:
    maior_peso = int(maior_peso)
    menor_peso = int(menor_peso)

print(f'O maior peso lido foi {maior_peso}Kg e o menor peso lido {menor_peso}Kg')
