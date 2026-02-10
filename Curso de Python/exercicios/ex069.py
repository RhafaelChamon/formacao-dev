"""Exercício Python 69: Crie um programa que leia a idade e o sexo de várias
   pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário
   quer ou não continuar. No final, mostre:
   A) quantas pessoas tem mais de 18 anos.
   B) quantos homens foram cadastrados.
   C) quantas mulheres tem menos de 20 anos."""

hom = mais18 = mul_men20 = 0
while True:
    print('-'*40)
    print(f'{'Cadastro de Pessoas':^40}')
    print('-'*40)
    while True:
        try:
            idade = int(input('Idade: '))
            break
        except ValueError:
            None
    while True:
        sexo = input('Sexo [M/F]: ').strip().upper()[0]
        if sexo == 'M' or sexo == 'F':
            break
    if idade >= 18:
        mais18 += 1
    if sexo == 'M':
        hom += 1
    if sexo == 'F' and idade < 20:
        mul_men20 += 1
    print('-'*40)
    while True:
        cont = input('Quer continuar [S/N]? ').strip().upper()
        if bool(cont) == True and cont[0] == 'N' or cont == 'S':
            break
    if cont == 'N':
        break
print(f'{' FIM DO PROGRAMA ':=^30}')
print(f'Total de pessoas com mais de 18 anos: {mais18}')
if hom == 0:
    print(f'Ao todo temos nenhum homem cadastrado')
elif hom == 1:
    print(f'Ao todo temos 1 homem cadastrado')
else:
    print(f'Ao todo temos {hom} homens cadastrados')
if mul_men20 == 0:
    print(f'E temos nenhuma mulher com menos de 20 anos')
elif mul_men20 == 1:
    print(f'E temos 1 mulher com menos de 20 anos')
else:
    print(f'E temos {mul_men20} mulheres com menos de 20 anos')
