"""Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
   No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais
   velho e quantas mulheres têm menos de 20 anos."""

S_idades = 0
hom_velho = 0
mul_men20 = 0
hom_velho_nome = ''
for c in range(1, 5):
    print(f'{c}ª Pessoa')
    nome = input(f'Digite o nome: ')
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo [M/F]: ')
    print()
    S_idades += idade
    if sexo == 'M' and idade > hom_velho:
        hom_velho = idade
        hom_velho_nome = nome
    if sexo == 'F' and idade < 20:
        mul_men20 += 1
print(f'\nA média da idade de todos do grupo é {S_idades / 4:.1f} anos')
print(f'O homem mais velho é o {hom_velho_nome} com {hom_velho} anos')
print(f'Existem {mul_men20} mulheres com menos de 20 anos')
