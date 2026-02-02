"""Exercício Python 93: Crie um programa que gerencie o aproveitamento de um
   jogador de futebol. O programa vai ler o nome do jogador e quantas partidas
   ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No
   final, tudo isso será guardado em um dicionário, incluindo o total de gols
   feitos durante o campeonato."""

jogador = dict()
jogador['nome'] = input('Qual o nome do jogador: ')
while True:
    try: jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? ')); break
    except ValueError: print('\033[1:31mINVÁLIDO!\033[m Tente novamente!', end=' ')
jogador['gols'] = list()
for k in range(0, jogador['partidas']):
    while True:
        try:
            jogador['gols'].append(int(input(f'Quantos gols {jogador["nome"]} fez na {k+1}ª partida? ')))
            break
        except ValueError: print('\033[1:31mINVÁLIDO!\033[m Tente novamente!', end=' ')

print(f'\n{jogador["nome"]} jogou {jogador["partidas"]} partidas. Fazendo: ')
for i in range(0, len(jogador["gols"])):
    print(f'      - Na {i+1}ª partida: {jogador["gols"][i]} gols')
print(f'    Ao todo, {jogador["nome"]} fez {sum(jogador["gols"])} gols')
