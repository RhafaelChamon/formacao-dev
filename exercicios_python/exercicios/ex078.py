"""Exercício Python 78: Faça um programa que leia 5 valores numéricos e guarde-os
   em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as
   suas respectivas posições na lista."""

lista = list()
for c in range(1, 6):
    while True:
        try:
            n = float(input(f'Digite o {c}º valor: '))
            if n % 1 == 0:
                lista.append(int(n))
            else:
                lista.append(n)
            break
        except ValueError:
            print('Invalido!', end=' ')
pos_max = list()
pos_min = list()
for c in range(0, 5):
    if lista[c] == max(lista):
        pos_max.append(str(c+1))
    if lista[c] == min(lista):
        pos_min.append(str(c+1))
if len(pos_max) > 1:
    print(f'O maior valor digitado foi {max(lista)} nas posições {', '.join(pos_max)}')
else:
    print(f'O maior valor digitado foi {max(lista)} na posição {''.join(pos_max)}')

if len(pos_min) > 1:
    print(f'O maior valor digitado foi {min(lista)} nas posições {', '.join(pos_min)}')
else:
    print(f'O maior valor digitado foi {min(lista)} na posição {''.join(pos_min)}')
