"""Exercício Python 71: Crie um programa que simule o funcionamento de um caixa
   eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado
   (número inteiro) e o programa vai informar quantas cédulas de cada valor
   serão entregues.

   OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1."""

print('='*56)
print(f'{'Banco Curso em Vídeo (CEV Bank)':^56}')
print('='*56)
while True:
    try:
        valor = int(input('Qual o valor do saque: R$'))
        print('')
        break
    except ValueError:
        print('Valor inválido! Tente outro valor. (Não use centavos!)')

"""sacar = valor
quant_200 = sacar // 200
sacar -= quant_200 * 200
quant_100 = sacar // 100
sacar -= quant_100 * 100
quant_50 = sacar // 50
sacar -= quant_50 * 50
quant_20 = sacar // 20
sacar -= quant_20 * 20
quant_10 = sacar // 10
sacar -= quant_10 * 10
quant_5 = sacar // 5
sacar -= quant_5 * 5
quant_2 = sacar // 2
sacar -= quant_2 * 2
quant_1 = sacar // 1
sacar -= quant_1 * 1
print(f'Para sacar R${valor}, você irá receber: ')
if quant_200 > 0:
    print(f'{quant_200} cédulas de R$200')
if quant_100 > 0:
    print(f'{quant_100} cédulas de R$100')
if quant_50 > 0:
    print(f'{quant_50} cédulas de R$50')
if quant_20 > 0:
    print(f'{quant_20} cédulas de R$20')
if quant_10 > 0:
    print(f'{quant_10} cédulas de R$10')
if quant_5 > 0:
    print(f'{quant_5} cédulas de R$5')
if quant_2 > 0:
    print(f'{quant_2} cédulas de R$2')
if quant_1 > 0:
    print(f'{quant_1} moedas de R$1')"""

print(f'Para sacar R${valor}, você irá receber: ')
saque = valor
ced = 200
while True:
    if saque >= ced:
        quant_ced = saque // ced
        saque -= quant_ced * ced
        if ced != 1:
            print(f'{quant_ced} cédulas de R${ced}' if quant_ced > 1 else f'{quant_ced} cédula de R${ced}')
        else:
            print(f'{quant_ced} moeda de R${ced}')
    else:
        if ced == 200:
            ced = 100
        elif ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        elif ced == 2:
            ced = 1
        elif ced == 1:
            break
print('='*56)
print('Volte sempre ao CEV Bank! Tenha um ótimo dia!')
