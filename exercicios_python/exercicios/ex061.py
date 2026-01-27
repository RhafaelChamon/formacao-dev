"""Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
   mostrando os 10 primeiros termos da progressão usando a estrutura while."""

print('-=-'*20)
print(f'|{'Calculadora de PA - v2.0':^58}|')
print('-=-'*20)

a_1 = float(input('Qual o primeiro termo (a1)? '))
r = float(input('Qual a razão dessa PA? '))

if a_1 % 1 == 0 and r % 1 ==0:
    a_1 = int(a_1)
    r = int(r)

print('Aqui estão os 10 primeiros termos dessa PA: ')
print(f'{a_1}', end = '')
c = 2
while c <= 10:
    print(f', {a_1 + r * (c-1)}', end = '')
    c += 1
