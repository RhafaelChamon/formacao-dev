"""Exercício Python 80: Crie um programa onde o usuário possa digitar cinco
   valores numéricos e cadastre-os em uma lista, já na posição correta de
   inserção (sem usar o sort()). No final, mostre a lista ordenada na tela."""

lista = list()
for i in range(1, 6):
    while True:
        try:
            n = float(input(f'Digite o {i}º valor numérico: '))
            break
        except ValueError:
            print('Inválido!', end=' ')
    if n % 1 == 0:
        n = int(n)
    if len(lista) == 0:
        lista.append(n)
        print('Valor adicionado na lista!')
    else:
        for k in range(0, len(lista)):
            if n in lista:
                print('O valor já está na lista!')
                break
            elif n > max(lista):
                lista.append(n)
                print('Valor adicionado no final da lista!')
                break
            else:
                if n < lista[k]:
                    lista.insert(k, n)
                    print(f'Valor adicionado na posição {k+1} da lista!')
                    break
    print()
for i in range(0, len(lista)):
    lista[i] = str(lista[i])
print('-='*30, end='\n')
print(f'Os valores digitados em ordem crescente é {", ".join(lista)}')
