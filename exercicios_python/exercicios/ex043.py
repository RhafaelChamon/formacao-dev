"""Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
   calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
   – IMC abaixo de 18,5: Abaixo do Peso
   – Entre 18,5 e 25: Peso Ideal
   – 25 até 30: Sobrepeso
   – 30 até 40: Obesidade
   – Acima de 40: Obesidade Mórbida """

print('\033[:32m=\033[m'*40)
print('\033[:32m|{:^38}|\033[m'.format('Calculadora de IMC'))
print('\033[:32m=\033[m'*40)
peso = float(input('Informe seu \033[1:31mpeso\033[m (Kg): '))
alt = float(input('Informe sua \033[1:33maltura\033[m (metros): '))
IMC = peso / (alt ** 2)
print('\nSua classificação de acordo com o seu IMC que é {:.1f} será:\n'.format(IMC))
if IMC < 18.5:
    print('|\033[1:31m{:<55}\033[m|'.format('Abaixo do Peso (Abaixo de 18.5)'))
    print('|{:<55}|'.format('Peso normal (18.5 - 24.9)'))
    print('|{:<55}|'.format('Sobrepeso (25 - 29.9)'))
    print('|{:<55}|'.format('Obesidade Grau I (30 - 34.9)'))
    print('|{:<55}|'.format('Obesidade Grau II (35 - 39.9)'))
    print('|{:<55}|'.format('Obesidade Grau III\\Obesidade Mórbita (40 ou mais)'))
elif IMC >= 18.5 and IMC < 25:
    print('|{:<55}|'.format('Abaixo do Peso (Abaixo de 18.5)'))
    print('|\033[1:32m{:<55}\033[m|'.format('Peso normal (18.5 - 24.9)'))
    print('|{:<55}|'.format('Sobrepeso (25 - 29.9)'))
    print('|{:<55}|'.format('Obesidade Grau I (30 - 34.9)'))
    print('|{:<55}|'.format('Obesidade Grau II (35 - 39.9)'))
    print('|{:<55}|'.format('Obesidade Grau III\\Obesidade Mórbita (40 ou mais)'))
elif IMC >= 25 and IMC < 30:
    print('|{:<55}|'.format('Abaixo do Peso (Abaixo de 18.5)'))
    print('|{:<55}|'.format('Peso normal (18.5 - 24.9)'))
    print('|\033[1:33m{:<55}\033[m|'.format('Sobrepeso (25 - 29.9)'))
    print('|{:<55}|'.format('Obesidade Grau I (30 - 34.9)'))
    print('|{:<55}|'.format('Obesidade Grau II (35 - 39.9)'))
    print('|{:<55}|'.format('Obesidade Grau III\\Obesidade Mórbita (40 ou mais)'))
elif IMC >= 30 and IMC < 35:
    print('|{:<55}|'.format('Abaixo do Peso (Abaixo de 18.5)'))
    print('|{:<55}|'.format('Peso normal (18.5 - 24.9)'))
    print('|{:<55}|'.format('Sobrepeso (25 - 29.9)'))
    print('|\033[1:33m{:<55}\033[m|'.format('Obesidade Grau I (30 - 34.9)'))
    print('|{:<55}|'.format('Obesidade Grau II (35 - 39.9)'))
    print('|{:<55}|'.format('Obesidade Grau III\\Obesidade Mórbita (40 ou mais)'))
elif IMC >= 35 and IMC < 40:
    print('|{:<55}|'.format('Abaixo do Peso (Abaixo de 18.5)'))
    print('|{:<55}|'.format('Peso normal (18.5 - 24.9)'))
    print('|{:<55}|'.format('Sobrepeso (25 - 29.9)'))
    print('|{:<55}|'.format('Obesidade Grau I (30 - 34.9)'))
    print('|\033[1:31m{:<55}\033[m|'.format('Obesidade Grau II (35 - 39.9)'))
    print('|{:<55}|'.format('Obesidade Grau III\\Obesidade Mórbita (40 ou mais)'))
else:
    print('|{:<55}|'.format('Abaixo do Peso (Abaixo de 18.5)'))
    print('|{:<55}|'.format('Peso normal (18.5 - 24.9)'))
    print('|{:<55}|'.format('Sobrepeso (25 - 29.9)'))
    print('|{:<55}|'.format('Obesidade Grau I (30 - 34.9)'))
    print('|{:<55}|'.format('Obesidade Grau II (35 - 39.9)'))
    print('|\033[1:31m{:<55}\033[m|'.format('Obesidade Grau III\\Obesidade Mórbita (40 ou mais)'))
