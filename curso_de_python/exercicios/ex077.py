"""Exercício Python 77: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
   Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais."""

palavras = ('lapis', 'aprender', 'programar', 'pc gamer', 'python',
            'curso', 'Cev', 'C#', 'curso', 'mercado', 'emprego')
for i in palavras:
    print(f'Na palavra {i.upper()} temos as vogais:', end=' ')
    vog = 0
    for letra in i.upper():
        if letra in 'AEIOU':
            print(letra, end=' ')
            vog += 1
    if vog == 0:
        print('N/A', end=' ')
    print('')
