"""Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário
   e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule
   um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%."""

from re import findall

sal = findall(r'\d+', input('Qual o salário do funcionário? '))
if sal:
    if len(sal) == 1:
        sal = float(sal[0])
    else:
        sal = float(".".join(sal[:2]))

    if sal >= 1250:
        print('Esse funcionário recebe R${:.2f} e com o aumento passará a receber R${:.2f}'.format(sal, (sal + sal * 10 / 100)))
    else:
        print('Esse funcionário recebe R${:.2f} e com o aumento passará a receber R${:.2f}'.format(sal, (sal + sal * 15 / 100)))
