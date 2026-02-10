"""Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
   O programa encerrará quando ele disser que quer mostrar 0 termos. """

print('-=-'*20)
print(f'|{'Calculadora de PA - v3.0':^58}|')
print('-=-'*20)

a_1 = float(input('Qual o primeiro termo (a1)? '))
r = float(input('Qual a razão dessa PA? '))

if a_1 % 1 == 0 and r % 1 ==0:
    a_1 = int(a_1)
    r = int(r)

termos = 10
print('Aqui estão os 10 primeiros termos dessa PA: ')
print(f'{a_1}', end = '')
c = 2
while c <= termos:
    print(f', {a_1 + r * (c-1)}', end = '')
    c += 1
print('')

termos += int(input('Gostaria de ver mais quantos dessa PA (digite 0 para nenhum)? '))
print(f'{a_1 + r * (c-1)}', end = '')
c += 1
while c <= termos:
    print(f', {a_1 + r * (c-1)}', end = '')
    c += 1
