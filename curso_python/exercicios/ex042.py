"""Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o
   recurso de mostrar que tipo de triângulo será formado:
   – EQUILÁTERO: todos os lados iguais
   – ISÓSCELES: dois lados iguais, um diferente
   – ESCALENO: todos os lados diferentes """

l1 = float(input('Informe um lado do triângulo: '))
l2 = float(input('Informe outro lado do triângulo: '))
l3 = float(input('Informe o último lado do triângulo: '))

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    if l1 == l2 and l2 == l3:
        tipo = 'equilátero'
    elif l1 != l2 and l2 != l3 and l1 != l3:
        tipo = 'escaleno'
    else:
        tipo = 'isósceles'

    print('É possível sim formar um triângulo de lados {}, {}, {} e ele é um triângulo {}'.format(l1, l2, l3, tipo))
else:
    print('Não é possível formar um triângulo de lados {}, {}, {}'.format(l1, l2, l3))
