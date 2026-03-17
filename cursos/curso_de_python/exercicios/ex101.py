"""Exercício Python 101: Crie um programa que tenha uma função chamada voto()
   que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando
   um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e
   OBRIGATÓRIO nas eleições."""

def voto(ano_nasc):
    from time import strftime, localtime

    ano_atual = int(strftime('%Y', localtime()))
    idade = ano_atual - ano_nasc
    if idade < 16:
        return f'Quem tem {idade} anos, \033[1:31mNÃO VOTA.\033[m'
    elif 16 <= idade < 18 or idade >= 70:
        return f'Quem tem {idade} anos, \033[1:33mVOTO É OPCIONAL.\033[m'
    else:
        return f'Quem tem {idade} anos, \033[1:32mVOTO É OBRIGATÓRIO.\033[m'


while True:
    try: nasc = int(input('Digite o ano de nascimento: ')); break
    except ValueError: print('\033[1:31mINVÁLIDO!\033[m Tente novamente.', end=' ')
print(voto(nasc))
