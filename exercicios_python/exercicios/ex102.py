"""Exercício Python 102: Crie um programa que tenha uma função fatorial() que
   receba dois parâmetros: o primeiro que indique o número a calcular e outro
   chamado show, que será um valor lógico (opcional) indicando se será mostrado
   ou não na tela o processo de cálculo do fatorial."""

def fatorial(n, show=False):
    """ -> Cálcula o fatorial de um número 'n'.
    :param n: Valor a fatorar
    :param show: Se verdadeiro, monstra o cálculo (opcional)
    :return: Retorna o valor do fatorial de 'n'
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            if c != 1: print(f'{c} x ', end='')
            else: print(f'{c} = ', end='')
    return f


print(fatorial(5, True))
#help(fatorial)
