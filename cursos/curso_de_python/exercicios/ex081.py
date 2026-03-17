"""Exercício Python 81: Crie um programa que vai ler vários números e colocar
   em uma lista. Depois disso, mostre:
   A) Quantos números foram digitados.
   B) A lista de valores, ordenada de forma decrescente.
   C) Se o valor 5 foi digitado e está ou não na lista."""

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
    lista.append(n)
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
print('-='*30, end='\n')
lista_copy = sorted(lista.copy(), reverse=True)
for i in range(0, len(lista_copy)):
    lista_copy[i] = str(lista_copy[i])
print(f'Foram digitados {len(lista)} números\n'
      f'A lista em ordem decrescente é {", ".join(lista_copy)}')
if lista.count(5) == 0:
    print('O valor 5 não está na lista')
else:
    print(f'O valor 5 está na lista e na posição {lista.index(5)+1}')
