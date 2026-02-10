"""Exercício Python 40: Crie um programa que leia duas notas de um aluno e calcule sua média,
   mostrando uma mensagem no final, de acordo com a média atingida:
   – Média abaixo de 5.0: REPROVADO
   – Média entre 5.0 e 6.9: RECUPERAÇÃO
   – Média 7.0 ou superior: APROVADO"""

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
M = (n1 + n2)/2
if M < 5:
    print('Aluno \033[1:31mREPROVADO\033[m')
elif M >= 5 and M < 7:
    print('Aluno \033[1:33mRECUPERADO\033[m')
else:
    print('Aluno \033[1:32mAPROVADO\033[m')
