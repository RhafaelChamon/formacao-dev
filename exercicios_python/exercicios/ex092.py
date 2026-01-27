"""Exercício Python 92: Crie um programa que leia nome, ano de nascimento e
   carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso
   a CTPS for diferente de ZERO, o dicionário receberá também o ano de
   contratação e o salário. Calcule e acrescente, além da idade, com quantos
   anos a pessoa vai se aposentar."""

from time import strftime, localtime

individuo = {}

print(f'{" INSS DO FUTURO ":=^40}\n')

individuo['nome'] = input('Nome: ')
while True:
    try: individuo['ano_nasc'] = int(input('Ano de nascimento: ')); break
    except ValueError: print(f'\033[1:31mINVÁLIDO!\033[m Tente novamente.')
individuo['ctps'] = input('Número da carteira de trabalho (se não possuir pressione ENTER): ')
if bool(individuo['ctps']):
    while True:
        try: individuo['ano_contrato'] = int(input('Ano de contrato: ')); break
        except ValueError: print(f'\033[1:31mINVÁLIDO!\033[m Tente novamente.')
    while True:
        try: individuo['salario'] = float(input('Salário: R$')); break
        except ValueError: print(f'\033[1:31mINVÁLIDO!\033[m Tente novamente.')
individuo['idade'] = int(strftime('%Y', localtime())) - individuo['ano_nasc']

print(f'\n{" Informações ":=^40}\n')
if not bool(individuo['ctps']):
    print(f'{individuo["nome"]} tem {individuo["idade"]} anos, e não possuí CTPS.')
else:
    print(f'{individuo["nome"]} tem {individuo["idade"]} anos, possuí carteira de trabalho Nº{individuo["ctps"]}.\n'
          f'Contratado em {individuo["ano_contrato"]}, com salário de R${individuo["salario"]:.2f}.\n'
          f'Irá se aposentar em {individuo["ano_contrato"]+35}, '
          f'com {individuo["ano_contrato"] + 35 - individuo["ano_nasc"]} anos.')
