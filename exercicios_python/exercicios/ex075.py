"""Exercício Python 75: Desenvolva um programa que leia quatro valores pelo teclado e
   guarde-os em uma tupla.No final, mostre:
   a) Quantas vezes apareceu o valor 9.
   b) Em que posição foi digitado o primeiro valor 3.
   c) Quais foram os números pares."""

n = (int(input('Digite um número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite mais um número: ')),
     int(input('Digite o último número: ')))

if n.count(9) == 0:
    print('O número 9 foi digitado nenhuma vez')
elif n.count(9) == 1:
    print('O número 9 foi digitado uma vez')
else:
    print(f'O número 9 foi digitado {n.count(9)} vezes')

if n.count(3) != 0:
    print(f'O número 3 foi digitado na posição {n.index(3)+1}')
else:
    print('O número 3 foi digitado nenhuma vez')

pares = 0
for c in n:
    if c % 2 == 0:
        pares += 1
if pares == 0:
    print('Foi digitado nenhum número par')
elif pares == 1:
    print('Foi digitado o número par', end=' ')
    for c in n:
        if c % 2 == 0:
            print(c)
else:
    print('Foi digitado os números pares', end=' ')
    for c in n:
        if c % 2 == 0:
            print(c, end=' ')
