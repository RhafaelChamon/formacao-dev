"""Exercício Python 86: Crie um programa que declare uma matriz de dimensão 3×3
   e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela,
   com a formatação correta."""

m = [[], [], []]
i = [[], [], []]

for l in range(0, 3):
    for c in range(0, 3):
        n = input(f'Digite um valor para a posição ({l+1}, {c+1}): ')
        m[l].append(n)
for c in range(0, 3):
    for l in range(0, 3): i[c].append(len(m[l][c]))

k = f'--{"-" * max(i[0])}---{"-" * max(i[1])}---{"-" * max(i[2])}--'

print(f'\n{"MATRIZ 3x3":^{len(k)}}')
print(k)
for l in range(0, 3):
    print(f'|{m[l][0]:^{max(i[0]) + 2}}|{m[l][1]:^{max(i[1]) + 2}}|{m[l][2]:^{max(i[2]) + 2}}|')
    print(k)
