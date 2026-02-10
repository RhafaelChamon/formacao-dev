"""Exercício Python 87: Aprimore o desafio anterior, mostrando no final:
   A) A soma de todos os valores pares digitados.
   B) A soma dos valores da terceira coluna.
   C) O maior valor da segunda linha."""

m = [[], [], []]
j = [[], [], []]

for l in range(0, 3):
    for c in range(0, 3):
        while True:
            n = input(f'Digite um valor para a posição ({l+1}, {c+1}): ')
            m[l].append(n)
            try: n = int(n); break
            except ValueError: print('\033[1:31mERRO!\033[m Tente novamente!'); del m[l][-1]
for c in range(0, 3):
    for l in range(0, 3): j[c].append(len(m[l][c]))

k = f'--{"-" * max(j[0])}---{"-" * max(j[1])}---{"-" * max(j[2])}--'

print(f'\n{"=-" * len(k) * 2}\n\n{"MATRIZ 3x3":^{len(k)}}')
print(k)
for l in range(0, 3):
    print(f'|{m[l][0]:^{max(j[0]) + 2}}|{m[l][1]:^{max(j[1]) + 2}}|{m[l][2]:^{max(j[2]) + 2}}|')
    print(k)
print(f'\n{'=-' * len(k) * 2}\n')

soma_par = soma_c3 = mai_l2 = 0
for l in range(0, 3):
    for c in range(0, 3):
        if int(m[l][c]) % 2 == 0: soma_par += int(m[l][c])
        if c == 2:  soma_c3 += int(m[l][c])
        if l == 1:
            if c == 0 or int(m[l][c]) > mai_l2: mai_l2 = int(m[l][c])

print(f'A soma de todos os valores pares digitados é {soma_par}\n'
      f'A soma dos valores da terceira coluna é {soma_c3}.\n'
      f'O maior valor da segunda linha é {mai_l2}.')
