"""Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você."""

from emoji import emojize
from random import randint
from time import sleep

print('\033[1:33m-=-\033[:36m-=-\033[m' * 11)
print('\033[:36m|\033[m{:^58}\033[1:33m|\033[m'.format(emojize(':scissors::page_with_curl::rock: Pedra - Papel - '
                                                           'Tesoura :rock::page_with_curl::scissors:')))
print('\033[1:33m-=-\033[:36m-=-\033[m' * 11)
print('Vamos jogar Pedra {}, Papel {}, Tesoura {} (também conhecido como Jokenpô), vamos lá?'.
      format(emojize(':rock:'), emojize(':page_with_curl:'), emojize(':scissors:')))
while True:
    print('Vou começar...')
    bot = randint(1, 3)
    sleep(3.5)
    print('Pronto! Já escolhi o que quero jogar, agora é sua vez! O que gostaria de jogar? ')
    sleep(1)
    print('[1] Pedra {}\n'
          '[2] Papel {}\n'
          '[3] Tesoura {}'.format(emojize(':rock:'), emojize(':page_with_curl:'), emojize(':scissors:')))
    jog = int(input('Sua escolha: '))
    sleep(1)
    print('\nPEDRA {}'.format(emojize(':rock:')))
    sleep(1)
    print('PAPEL {}'.format(emojize(':page_with_curl:')))
    sleep(1)
    print('TESOOOUU...', end = '')
    sleep(1.4)
    print('RA! {}\n'.format(emojize(':scissors:')))
    if jog >= 1 and jog <= 3:
        if bot == 1 and jog == 1:
            print('Quase! Empatamos! Eu joguei pedra e você também {}x{}'.format(emojize(':rock:'), emojize(':rock:')))
            print ('Fim da rodada: \033[1:33mEMPATE...\033[m')
        elif bot == 1 and jog == 2:
            print('Parabéns! Você ganhou! Eu joguei pedra e você papel {}x{}'.format(emojize(':rock:'), emojize(':page_with_curl:')))
            print('Fim da rodada: \033[1:32mVITÓRIA...\033[m')
        elif bot == 1 and jog == 3:
            print('Uruuh! Eu ganhei! Eu joguei pedra e você tesoura {}x{}'.format(emojize(':rock:'), emojize(':scissors:')))
            print('Fim da rodada: \033[1:31mDERROTA...\033[m')
        elif bot == 2 and jog == 1:
            print('Uruuh! Eu ganhei! Eu joguei papel e você pedra {}x{}'.format(emojize(':page_with_curl:'), emojize(':rock:')))
            print('Fim da rodada: \033[1:31mDERROTA...\033[m')
        elif bot == 2 and jog == 2:
            print('Quase! Empatamos! Eu joguei papel e você também {}x{}'.format(emojize(':page_with_curl:'), emojize(':page_with_curl:')))
            print('Fim da rodada: \033[1:33mEMPATE...\033[m')
        elif bot == 2 and jog == 3:
            print('Parabéns! Você ganhou! Eu joguei papel e você tesoura {}x{}'.format(emojize(':page_with_curl:'), emojize(':scissors:')))
            print('Fim da rodada: \033[1:32mVITÓRIA...\033[m')
        elif bot == 3 and jog == 1:
            print('Parabéns! Você ganhou! Eu joguei tesoura e você pedra {}x{}'.format(emojize(':scissors:'), emojize(':rock:')))
            print('Fim da rodada: \033[1:32mVITÓRIA...\033[m')
        elif bot == 3 and jog == 2:
            print('Uruuh! Eu ganhei! Eu joguei tesoura e você papel {}x{}'.format(emojize(':scissors:'), emojize(':page_with_curl:')))
            print('Fim da rodada: \033[1:31mDERROTA...\033[m')
        elif bot == 3 and jog == 3:
            print('Quase! Empatamos! Eu joguei tesoura e você também {}x{}'.format(emojize(':scissors:'), emojize(':scissors:')))
            print('Fim da rodada: \033[1:33mEMPATE...\033[m')
        else:
            print('Erro desconhecido! {}'.format(emojize(':prohibited:')))
    else:
        print('Jogada inválida! {}'.format(emojize(':prohibited:')))
        print('Fim da rodada: \033[1:31mDERROTA...\033[m')
    print(f'{'-' * 30}\nDeseja jogar novamente?\n[1] Sim\n[2] Não\n{"-" * 30}')
    while True:
        cont = input('Sua resposta:')
        if cont[0] in '12':
            break
        else:
            print('Inválido!', end=' ')
    if cont[0] == '2':
        break
    sleep(1)
    print('\nEntão vamos mais uma rodada!')
