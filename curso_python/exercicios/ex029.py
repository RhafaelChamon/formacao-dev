"""Exercício Python 29: Escreva um programaque leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
   mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite."""

from re import findall

vel = input('- Radar 80Km/h - Qual a velocidade do carro? ')
vform = findall('\\d+', vel)
if vform:
    vform = int(vform[0])
    if vform <= 80:
        print('Velocidade {}Km/h (Normal).'.format(vform))
    else:
        print('Velocidade {}Km/h (ALTA VELOCIDADE - Multa: R${:.2f}).'.format(vform, (vform - 80)*7))
else:
    print('ERRO INESPERADO: Nenhuma velocidade foi inserida.')
