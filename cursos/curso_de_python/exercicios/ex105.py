""""Exercício Python 105: Faça um programa que tenha uma função notas() que
   pode receber várias notas de alunos e vai retornar um dicionário com as
   seguintes informações:
   – Quantidade de notas
   – A maior nota
   – A menor nota
   – A média da turma
   – A situação (opcional)"""

def notas(notas_turma, sit=False):
    """
    :param notas_turma: Recebe as notas de turma em uma lista
    :param sit: Se verdadeiro, monstra a situação da turma
    :return: Retorna os dados da turma, em um dicionário
    """
    turma = dict()
    turma['total'] = len(notas_turma)
    turma['maior'] = max(notas_turma)
    turma['menor'] = min(notas_turma)
    turma['média'] = float(str(f'{sum(notas_turma) / len(notas_turma):.2f}'))
    if sit:
        if turma['média'] >= 7: turma['situação'] = 'BOA'
        elif turma['média'] >= 5: turma['situação'] = 'MÉDIA'
        else: turma['situação'] = 'RUIM'
    return turma


x = notas([10.0, 9.4, 0, 5.3, 10, 10.0], True)
print(x, f'\n{"-"*80}')
help(notas)
