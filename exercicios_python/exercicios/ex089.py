"""Exercício Python 89: Crie um programa que leia nome e duas notas de vários
   alunos e guarde tudo em uma lista composta. No final, mostre um boletim
   contendo a média de cada um e permita que o usuário possa mostrar as notas
   de cada aluno individualmente."""

print(f'{" ESCOLA IMPACTO ":=^40}')

alunos = []
while True:
    print(f'\nAluno {len(alunos)+1}: ------')
    nome = input('Nome: ')
    while True:
        try: nota1 = float(input('Nota 1: ')); break
        except ValueError: print('\033[1:31mERRO!\033[m Tente novamente!')
    while True:
        try: nota2 = float(input('Nota 2: ')); break
        except ValueError: print('\033[1:31mERRO!\033[m Tente novamente!')
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media].copy())
    while True:
        cont = input('Quer continuar? [S/N] ').upper().strip()
        if bool(cont) == True and cont[0] in 'SN': break
        else: print('\033[1:31mERRO!\033[m Tente novamente!')
    if cont == 'N':  break

if len(str(len(alunos))) > 2: alin_ID = len(str(len(alunos)))
else: alin_ID = 2
alin_nome = []
for i in range (0, len(alunos)):  alin_nome.append(len(alunos[i][0]))
if max(alin_nome) < 4: alin_nome.append(4)
x = f'{"ID":>{alin_ID}}   {"Nome":<{max(alin_nome)}}   Média'

print(f'\n{" ESCOLA IMPACTO ":=^40}\n')
print(f'{x}')
print('-' * len(x))
for i in range(0, len(alunos)):
    print(f'{str(i + 1):>{alin_ID}}   {alunos[i][0]:<{max(alin_nome)}}   {alunos[i][2]:.1f}')
print(f'\n{'=' * 40}')

print('\nSe quiser ver a nota individual, digite o ID do aluno (pressione ENTER para sair):', end=' ')
while True:
    ID = input()
    if not bool(ID): break
    else:
        try:
            ID = int(ID)
            if 0 < ID <= len(alunos):
                print(f'\nAluno:  {alunos[ID-1][0]}'
                      f'\nNota 1: {alunos[ID-1][1][0]}'
                      f'\nNota 2: {alunos[ID-1][1][1]}'
                      f'\nMédia:  {alunos[ID-1][2]}')
                print(f'\n{'=' * 40}')
                print('\nDigite o ID de outro aluno (pressione ENTER para sair):',
                      end=' ')
            else: print('\033[1:31mALUNO NÃO ENCONTRADO!\033[m Informe um ID válido:', end=' ')
        except ValueError: print('\033[1:31mERRO!\033[m Informe um ID válido:', end=' ')

print(f'\n{" PROGRAMA ENCERRADO ":=^40}\n')
