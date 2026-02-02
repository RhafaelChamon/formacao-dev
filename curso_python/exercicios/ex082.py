"""Exercício Python 82: Crie um programa que vai ler vários números e colocar
   em uma lista. Depois disso, crie duas listas extras que vão conter apenas
   os valores pares e os valores ímpares digitados, respectivamente.
   Ao final, mostre o conteúdo das três listas geradas."""

lista_geral = list()
lista_par = list()
lista_impar = list()
while True:
    while True:
        try:
            n = float(input('Digite um valor numérico: '))
            break
        except ValueError:
            print('Inválido!', end=' ')
    if n % 1 == 0:
        n = int(n)
    lista_geral.append(n)
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
for i in range(0, len(lista_geral)):
    if lista_geral[i] % 2 == 0:
        lista_par.append(str(lista_geral[i]))
    else:
        lista_impar.append(str(lista_geral[i]))
    lista_geral[i] = str(lista_geral[i])
print('-='*30)
print(f'A lista com todos os números digitados é {', '.join(lista_geral)}\n'
      f'A lista somente com os números pares é {', '.join(lista_par)}\n'
      f'A lista somente com os números ímpares é {', '.join(lista_impar)}\n')
