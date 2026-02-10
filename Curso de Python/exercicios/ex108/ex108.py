"""Exercício Python 108: Adapte o código do desafio #107, criando uma função
   adicional chamada moeda() que consiga mostrar os números como um valor
   monetário formatado."""

from moeda import *

while True:
    try: p = float(input("Digite um valor: R$")); break
    except ValueError: print('\033[1:31mINVÁLIDO!\033[m Tente novamente.')
print(f'Aumentando 10% de {moeda(p)}, temos {moeda(aumentar(p, 10))}')
print(f'Diminuindo 13% de {moeda(p)}, temos {moeda(diminuir(p, 13))}')
print(f'O dobro de {moeda(p)} é {moeda(dobro(p))}')
print(f'A metade de {moeda(p)} é {moeda(metade(p))}')
