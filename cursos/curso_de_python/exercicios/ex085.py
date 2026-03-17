"""Exercício Python 85: Crie um programa onde o usuário possa digitar sete
   valores numéricos e cadastre-os em uma lista única que mantenha separados
   os valores pares e ímpares. No final, mostre os valores pares e ímpares
   em ordem crescente."""

num = [[], []]

for c in range(1, 8):
    while True:
        try: n = float(input(f'Digite o {c}º valor numérico: ')); break
        except ValueError: print('Inválido!', end=' ')
    if n % 1 == 0: n = int(n)
    if n % 2 == 0: num[0].append(n)
    else: num[1].append(n)
print(f'Os valores pares digitados foram em ordem crescente: {sorted(num[0])}')
print(f'Os valores ímpares digitados foram em ordem crescente: {sorted(num[1])}')
