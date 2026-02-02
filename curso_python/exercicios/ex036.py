"""Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
   Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
   A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado."""

from time import sleep

print('\033[:32m_{}\033[m'.format('-_'*20))
print('\033[:32m|\033[m\033[1:33m{:^39}\033[m\033[:32m|\033[m'.format('New House Bank'))
print('\033[:32m-{}\033[m'.format('_-'*20))

print('Vamos se você é apto para realizar um \033[31mempréstimo bancário\033[m, para financiar '
      'sua \033[1:35mNOVA CASA\033[m!\n')

valor = float(input('Qual o \033[1:33mvalor\033[m da casa que você deseja adquirir: R$'))
sal = float(input('Qual o seu \033[1:32msalário\033[m mensal: R$'))
ano = int(input('Em quantos \033[1:36manos\033[m você deseja pagar o valor da casa: '))

print('\033[:37m\nVERIFICANDO...\033[m')
sleep(5)

prestacao = valor / (ano*12)
if prestacao <= (sal*30/100):
    print('Seu empréstimo foi \033[1:32m\033[4mAPROVADO\033[m!')
else:
    print('Seu financiamento foi \033[1:31m\033[4mNEGADO\033[m!')
