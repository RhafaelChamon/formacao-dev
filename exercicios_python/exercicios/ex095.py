"""Exercício Python 95: Aprimore o desafio 93 para que ele funcione com vários
   jogadores, incluindo um sistema de visualização de detalhes do
   aproveitamento de cada jogador."""

time = list()
jogador = dict()

while True:
    jogador['nome'] = input('Qual o nome do jogador: ')
    while True:
        try: partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? ')); break
        except ValueError: print('\033[1:31mINVÁLIDO!\033[m Tente novamente!', end=' ')
    jogador['gols'] = list()
    for k in range(0, partidas):
        while True:
            try:
                jogador['gols'].append(int(input(f'Quantos gols {jogador["nome"]} fez na {k+1}ª partida? ')))
                break
            except ValueError: print('\033[1:31mINVÁLIDO!\033[m Tente novamente!', end=' ')
    time.append(jogador.copy())
    while True:
        cont = input('Deseja continuar [S/N]? ').strip().upper()
        if bool(cont) == True and cont[0] in 'SN': break
        else: print('\033[1:31mERRO!\033[m Informe se deseja continuar ou não.', end=' ')
    if cont[0] == 'N': break
    else: print()

if len(str(len(time))) > 2: alin_ID = len(str(len(time)))
else: alin_ID = 2
alin_nome = []
for i in time:  alin_nome.append(len(i['nome']))
if max(alin_nome) < 7: alin_nome.append(7)
x = f'{"ID":>{alin_ID}}   {"Jogador":<{max(alin_nome)}}   Total de Gols'

print(f'\n{" DADOS DO TIME ":=^{len(x) * 2}}\n')
print(x)
print('-' * len(x))
for i in range (0, len(time)):
    print(f'{str(i + 1):>{alin_ID}}   {time[i]['nome']:<{max(alin_nome)}}   '
          f'{str(sum(time[i]["gols"])):^13}')
print(f'\n{'=' * len(x) * 2}')

print('\nPara monstrar o levantamento de algum jogador, digite o respectivo '
      'ID (pressione ENTER para sair):', end=' ')
while True:
    ID = input()
    if not bool(ID): break
    else:
        try:
            ID = int(ID)
            if 0 < ID <= len(time):
                print(f'\nLevantamento de dados do {time[ID - 1]["nome"]}')
                for i in range(0, len(time[ID - 1]["gols"])):
                    print(f'      - Na {i + 1}ª partida fez {time[ID - 1]["gols"][i]} gols')
                print(f'\n{'=' * len(x) * 2}')
                print('\nDigite o ID de outro jogador (pressione ENTER para sair):',
                      end=' ')
            else: print('\033[1:31mJOGADOR NÃO ENCONTRADO!\033[m Informe um ID válido:', end=' ')
        except ValueError: print('\033[1:31mERRO!\033[m Informe um ID válido:', end=' ')
print(f'\n{" PROGRAMA ENCERRADO ":=^{len(x) * 2}}\n')
