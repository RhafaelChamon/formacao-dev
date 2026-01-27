"""Exercício Python 94: Crie um programa que leia nome, sexo e idade de várias
   pessoas, guardando os dados de cada pessoa em um dicionário e todos os
   dicionários em uma lista. No final, mostre:
   A) Quantas pessoas foram cadastradas
   B) A média de idade
   C) Uma lista com as mulheres
   D) Uma lista de pessoas com idade acima da média"""

cadastros = list()
pessoa = dict()
s = 0

while True:
    pessoa['nome'] = input('Nome: ').capitalize()
    while True:
        sexo = input('Sexo [M/F]: ').strip().upper()
        if bool(sexo) == True and sexo[0] in 'MF': pessoa['sexo'] = sexo[0]; break
        else: print('\033[1:31mERRO!\033[m Informe se o sexo é masculino ou feminino.', end=' ')
    while True:
        try: pessoa['idade'] = int(input('Idade: ')); break
        except ValueError: print('\033[1:31mERRO!\033[m Valor inválido.', end=' ')
    s += pessoa['idade']
    cadastros.append(pessoa.copy())
    while True:
        cont = input('Deseja continuar [S/N]? ').strip().upper()
        if bool(cont) == True and cont[0] in 'SN': break
        else: print('\033[1:31mERRO!\033[m Informe se deseja continuar ou não.', end=' ')
    if cont[0] == 'N': print(f'\n{"=" * 30}\n'); break
    else: print()
med_idade = s / len(cadastros)

print(f'Foram cadastradas {len(cadastros)} pessoas.')
print(f'A média da idade é {med_idade:.1f} anos.')
print(f'As mulheres cadastradas foram:')
for i in cadastros:
    if i['sexo'] == 'F':
        print(f'    - {i["nome"]}')
print(f'As pessoas com idade maior do que a média são:')
for i in cadastros:
    if i['idade'] >= med_idade:
        print(f'    - {i["nome"]} com {i["idade"]} anos.')
