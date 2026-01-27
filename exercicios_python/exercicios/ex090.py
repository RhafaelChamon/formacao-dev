"""Exercício Python 90: Faça um programa que leia nome e média de um aluno,
   guardando também a situação em um dicionário. No final, mostre o conteúdo
   da estrutura na tela."""

aluno = dict()
aluno['nome'] = str(input('Nome: '))
while True:
    try: aluno['média'] = float(input(f'Média do(a) {aluno["nome"]}: ')); break
    except ValueError: print(f'\033[1:31mValor inválido!\033[m Tente novamente.')
if aluno['média'] >= 6: aluno['situacao'] = '\033[1:32mAPROVADO\033[m'
elif aluno['média'] < 4: aluno['situacao'] = '\033[1:31mREPROVADO\033[m'
else: aluno['situacao'] = '\033[1:33mRECUPERAÇÃO\033[m'

print(f'{'=' * 20}\n'
      f'Aluno: {aluno['nome']}\n'
      f'Média: {aluno['média']}\n'
      f'Condição: {aluno["situacao"]}')
