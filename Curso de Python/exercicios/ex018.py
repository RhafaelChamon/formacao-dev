"""Exercício Python 18: Faça um programa que leia um ângulo qualquer e
   mostre na tela o valor do seno, cosseno e tangente desse ângulo.   """

from math import radians, sin, cos, tan
ang = float(input('Digite o valor do angulo: '))
sen = sin(radians(ang))
cose = cos(radians(ang))
tan = tan(radians(ang))
print('Temos que: \n Sen {}º = {:.2f} \n Cos {}º = {:.2f} \n Tan {}º = {:.2f}'.format(ang, sen, ang, cose, ang, tan))
