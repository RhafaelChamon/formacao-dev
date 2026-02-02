"""Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
   mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
   O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.   """

n = int(input('Digite um número inteiro: '))
maior = n
menor = n
quant_n = 1
soma = n

fim = input('Quer continuar? [S/N] ').upper()
while fim != 'N' and fim != 'S':
    print('Opção invalida. Tente novamente.')
    fim = input('Quer continuar? [S/N] ').upper()

if fim == 'S':
    while fim == 'S':
        n = int(input('Digite um número inteiro: '))
        if n > maior:
            maior = n
        if n < menor:
            menor = n
        quant_n += 1
        soma += n

        fim = input('Quer continuar? [S/N] ').upper()
        while fim != 'N' and fim != 'S':
            print('Opção invalida. Tente novamente.')
            fim = input('Quer continuar? [S/N] ').upper()

print(f'Você digitou {quant_n}, e a média entre todos os valores digitados é {soma / quant_n}')
print(f'O maior número digitado foi {maior} e o menor foi {menor}')
