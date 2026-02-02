"""Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções
   incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um
   programa que importe esse módulo e use algumas dessas funções."""

from moeda import *

while True:
    try: p = float(input("Digite um valor: R$")); break
    except (ValueError): print('\033[1:31mINVÁLIDO!\033[m Tente novamente.')
print(f'Aumentando 10% de R${p:.2f}, temos R${aumentar(p, 10):.2f}')
print(f'Diminuindo 13% de R${p:.2f}, temos R${diminuir(p, 13):.2f}')
print(f'O dobro de R${p:.2f} é R${dobro(p):.2f}')
print(f'A metade de R${p:.2f} é R${metade(p):.2f}')
