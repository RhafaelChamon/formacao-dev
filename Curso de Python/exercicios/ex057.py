"""Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
   Caso esteja errado, peça a digitação novamente até ter um valor correto."""
fim = 'false'
while fim == 'false':
    sexo = input("Digite o sexo da pessoa (M/F): ").strip().upper()[0]
    if sexo == "M" or sexo == "F":
        fim = 'true'
    else:
        print('Inválido! Digite somente "M" para Masculino e "F" para Feminino')
if sexo == "M":
    print('\nSexo gravado como Masculino!')
elif sexo == "F":
    print('Sexo gravado como Feminino!')
