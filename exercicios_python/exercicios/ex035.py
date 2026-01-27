"""Exercício Python 35: Desenvolva um programa que leia o comprimento de três
   retas e diga ao usuário se elas podem ou não formar um triângulo."""

l1 = float(input('Informe um lado do triângulo: '))
l2 = float(input('Informe outro lado do triângulo: '))
l3 = float(input('Informe o último lado do triângulo: '))

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print('É possível sim formar um triângulo de lados {}, {}, {}'.format(l1, l2, l3))
else:
    print('Não é possível formar um triângulo de lados {}, {}, {}'.format(l1, l2, l3))
