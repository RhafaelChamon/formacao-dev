"""Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto,
   considerando o seu preço normal e condição de pagamento:
   – à vista dinheiro/cheque: 10% de desconto
   – à vista no cartão: 5% de desconto
   – em até 2x no cartão: preço formal
   – 3x ou mais no cartão: 20% de juros """

preco = float(input('Qual o preço do produto? R$'))
print('Qual será a forma de pagamento?\n'
      '[1] À vista dinheiro/PIX (10% de desconto)\n'
      '[2] Cartão de Débito (5% de desconto)\n'
      '[3] Até 2x no cartão (Preço Formal)\n'
      '[4] 3x ou mais no cartão (20% de juros)')
pag = int(input('Escolha: '))
if pag == 1:
    print('Sua compra ficou por R${:.2f}'.format(preco - preco * 0.1))
elif pag == 2:
    print('Sua compra ficou por R${:.2f}'.format(preco - preco * 0.05))
elif pag == 3:
    print('Sua compra ficou por R${:.2f}'.format(preco))
elif pag == 4:
    print('Sua compra ficou por R${:.2f}'.format(preco + preco * 0.2))

else:
    print('Opção invalida! Compra cancelada.')
