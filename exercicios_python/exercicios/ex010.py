"""Exercício Python 10: Crie um programa que leia quanto dinheiro uma
   pessoa tem na carteira e mostre quantos dólares ela pode comprar."""

reais = float(input('Quantos reais você tem na carteira? R$'))
print('Com R${}, e o dólar a R$5.57 e o euro a R$6.45, você consegue comprar '
      'U${:.2f}, ou então €${:.2f}.'.format(reais, (reais/5.57), (reais/6.45)))
