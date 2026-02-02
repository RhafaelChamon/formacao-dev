"""Exercício Python 79: Crie um programa onde o usuário possa digitar vários
   valores numéricos e cadastre-os em uma lista. Caso o número já exista lá
   dentro, ele não será adicionado. No final, serão exibidos todos os valores
   únicos digitados, em ordem crescente."""

lista = list()
while True:
    while True:
        try:
            n = float(input('Digite um valor numérico: '))
            break
        except ValueError:
            print('Inválido!', end=' ')
    if n % 1 == 0:
        n = int(n)
    if n in lista:
        print('O valor já está na lista!')
    else:
        lista.append(n)
        print('Valor adicionado na lista!')
    while True:
        cont = input('Deseja continuar? [S/N]: ').strip().lower()
        if bool(cont) == True and cont[0] in 'sn':
            break
        else:
            print('Inválido!', end=' ')
    if cont == 'n':
        break
    else:
        print()
lista.sort()
for c in range(0, len(lista)):
    lista[c] = str(lista[c])
print('-='*30, end='\n')
print(f'Os valores digitados em ordem crescente é {", ".join(lista)}')
