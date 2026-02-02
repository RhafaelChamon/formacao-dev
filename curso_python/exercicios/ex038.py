"""Exercício Python 38: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
– O primeiro valor é maior
– O segundo valor é maior
– Não existe valor maior, os dois são iguais"""


n1 = int(input('Digite um numero inteiro: '))
n2 = int(input('Digite outro numero inteiro: '))
print('')
if n1 > n2:
    print('O primeiro número é maior que o segundo')
elif n1 < n2:
    print('O segundo número é maior que o primeiro')
else:
    print('Não existe um valor maior, os dois são iguais')
