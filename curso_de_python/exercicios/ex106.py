"""Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do
   Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o
   usuário digitar a palavra ‘FIM’, o programa se encerrará.
   OBS: use cores."""

def line(cor):
    print(f'\033[1:{cor}m{"=" * 80}\033[m')


def msg(mensagem, cor):
    line(cor)
    print(f'\033[1:{cor}m||\033[m \033[7:{cor}m{mensagem:^{74}}\033[m \033[1:{cor}m||\033[m')
    line(cor)


while True:
    msg('Sistema de ajuda: PyHELP', 32)
    fun = input('Função ou biblioteca (<FIM> para sair) >> ')
    print('\n')
    if fun.upper() == 'FIM':
        msg('Sistema encerrado', 31)
        break
    else:
        msg(f'Manual do comando "{fun}"', 36)
        help(fun)
        line(36)
    print()
