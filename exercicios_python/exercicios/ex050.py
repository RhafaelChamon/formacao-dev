"""Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma
   apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o. """
S = 0
for c in range(1, 7):
    n = int(input('Digite o {}o. número inteiro: '.format(c)))
    if n % 2 == 0:
        S = S + n
print(f'A soma entre os números pares informados é {S}')
