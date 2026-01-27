"""Exercício Python 70: Crie um programa que leia o nome e o preço de vários
   produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
   A) qual é o total gasto na compra.
   B) quantos produtos custam mais de R$1000.
   C) qual é o nome do produto mais barato."""

s = itens_maiores_que_1000 = valor_item_mais_barato = 0
print('-'*40)
print(f'{'LOJA SUPER BARATÃO':^40}')
print('-'*40)
while True:
    nome = str(input('Nome do produto: ')).strip().title()
    while True:
        try:
            valor = float(input('Valor do produto: R$'))
            break
        except ValueError:
            print('Preço inválido! Insira novamente.')
    if valor_item_mais_barato == 0 or valor < valor_item_mais_barato:
        valor_item_mais_barato = valor
        nome_item_mais_barato = nome
    s += valor
    if valor > 1000:
        itens_maiores_que_1000 += 1
    cont = str(input('Quer continuar? [S/N] ')).strip().upper()
    if bool(cont) == True and cont[0] == 'N':
        break
print(f'{' FIM DO PROGRAMA ':-^40}')
print(f'O total da compra foi R${s:.2f}')
print(f'Temos {itens_maiores_que_1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nome_item_mais_barato.lower()} que custa R${valor_item_mais_barato:.2f}')
