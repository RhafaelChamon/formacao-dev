"""Exercício Python 96: Faça um programa que tenha uma função chamada área(),
   que receba as dimensões de um terreno retangular (largura e comprimento) e
   mostre a área do terreno."""

def area(comp, larg):
    print(f'A área desse terreno {comp}m x {larg}m é igual a {comp * larg:.1f}m²')


print(f'{"CONTROLE DE TERRENOS":-^40}')
while True:
    try: x = float(input('Comprimento do terreno (metros): ')); break
    except ValueError: print('\033[1:31mINVÁLIDO!\033[m Tente novamente.', end=' ')
while True:
    try: y = float (input('Largura do terreno (metros): ')); break
    except ValueError: print('\033[1:31mINVÁLIDO!\033[m Tente novamente.', end=' ')
area(x, y)
