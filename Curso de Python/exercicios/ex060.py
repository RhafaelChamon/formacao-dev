"""Exercício Python 60: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
   5! = 5 x 4 x 3 x 2 x 1 = 120 """

print('-=-'*20)
print(f'|{'Calculadora de fatorial':^58}|')
print('-=-'*20)

n = int(input('Digite qual valor você gostaria de calcular o fatorial: '))
if n < 0:
    print(f'Não existe fatorial de números negativos ({n}!)')
elif n == 0:
    print('0! = 1')
elif n == 1:
    print('1! = 1')
else:
    fatorial = 1
    print(f'{n}! = ', end='')
    while n != 0:
        fatorial *= n
        if n != 1:
            print(f'{n} x ', end='')
        else:
            print(f'{n} = {fatorial}')
        n -= 1
