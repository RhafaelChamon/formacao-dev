"""Exercício Python 51: Desenvolva um programa que leia o primeiro termo e
   a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão"""

print('Tratando de PA...')
a_1 = float(input('Qual o primeiro termo (a1)? '))
r = float(input('Qual a razão dessa PA? '))

if a_1 % 1 == 0 and r % 1 ==0:
    a_1 = int(a_1)
    r = int(r)

print('Aqui estão os 10 primeiros termos dessa PA: ')
print(f'{a_1}', end = '')
for c in range(1, 10):
    print(f', {a_1 + r * (c)}', end = '')
