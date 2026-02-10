"""Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto
   adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa."""

"""from math import sqrt
c1 = float(input('Digite o valor de um dos catetos do triângulo: '))
c2 = float(input('Digite o valor do outro cateto do triângulo: '))
h = sqrt(c1 ** 2 + c2 ** 2)
print('Esse triângulo retângulo de catetos medindo {} e {}, tem hipotenusa igual a {:.2f}.'.format(c1, c2, h))"""

import math
c1 = float(input('Digite o valor de um dos catetos do triângulo: '))
c2 = float(input('Digite o valor do outro cateto do triângulo: '))
hip = math.hypot(c1, c2)
print('Esse triângulo retângulo de catetos medindo {} e {}, tem hipotenusa igual a {:.2f}.'.format(c1, c2, hip))
