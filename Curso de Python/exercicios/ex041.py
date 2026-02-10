"""Exercício Python 41: A Confederação Nacional de Natação precisa de um programa que leia o ano de
   nascimento de um atleta e mostre sua categoria, de acordo com a idade:
   – Até 9 anos: MIRIM
   – Até 14 anos: INFANTIL
   – Até 19 anos: JÚNIOR
   – Até 25 anos: SÊNIOR
   – Acima de 25 anos: MASTER
   """

from datetime import datetime

print('\033[:34m=\033[m'*40)
print('\033[:34m|{:^38}|\033[m'.format('Confederação Nacional de Natação'))
print('\033[:34m=\033[m'*40)

ano_atual = datetime.now().year
ano_nasc = int(input('Digite o ano de \033[:32mnascimento\033[m: '))
idade = ano_atual - ano_nasc
if idade <= 9:
    mod = '\033[1:35mMIRIM\033[m'
elif idade > 9 and idade <= 14:
    mod = '\033[1:36mINFANTIL\033[m'
elif idade > 14 and idade <= 19:
    mod = '\033[1:32mJÚNIOR\033[m'
elif idade > 19 and idade <= 25:
    mod = '\033[1:33mSÊNIOR\033[m'
else:
    mod = '\033[1:31mMASTER\033[m'
print('Este atleta tem {} anos, e neste ano de {} irá concorrer na modalidade {}'.format(idade, ano_atual, mod))
