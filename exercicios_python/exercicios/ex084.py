"""Exercício Python 84: Faça um programa que leia nome e peso de várias pessoas,
   guardando tudo em uma lista. No final, mostre:
   A) Quantas pessoas foram cadastradas.
   B) Uma listagem com as pessoas mais pesadas.
   C) Uma listagem com as pessoas mais leves."""

pessoas = list()
cadastro = list()

while True:
    cadastro.append(input('Nome: '))
    while True:
        try: cadastro.append(float(input('Peso(Kg): '))); break
        except ValueError: print('Inválido!', end=' ')
    pessoas.append(cadastro.copy())
    cadastro.clear()
    while True:
        cont = input('Deseja continuar? [S/N] ').upper().strip()
        if bool(cont) == True and cont[0] in 'SN': break
        else: print('\033[1:31mERRO!\033[m Tente novamente!')
    if cont == 'N':  break

print('-='*30)
print(f'Foram cadastrados um total de {len(pessoas)} pessoas.')
for c in range(0, len(pessoas)):
    if c == 0: pesado = leve = pessoas[c][1]
    elif pessoas[c][1] > pesado: pesado = pessoas[c][1]
    elif pessoas[c][1] < leve: leve = pessoas[c][1]
print(f'O(s) mais pesado(s) com {pesado}Kg é ou são:', end=' ')
k = 0
for c in range(0, len(pessoas)):
    if pessoas[c][1] == pesado:
        if k == 0: print(f'{pessoas[c][0]} ', end='')
        else: print(f', {pessoas[c][0]} ', end='')
        k += 1
print()
print(f'O(s) mais leve(s) com {leve}Kg é ou são:', end=' ')
k = 0
for c in range(0, len(pessoas)):
    if pessoas[c][1] == leve:
        if k == 0: print(f'{pessoas[c][0]} ', end='')
        else: print(f', {pessoas[c][0]} ', end='')
        k += 1
