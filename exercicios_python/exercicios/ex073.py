"""Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da
   Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
   a) Os 5 primeiros times.
   b) Os últimos 4 colocados.
   c) Times em ordem alfabética.
   d) Em que posição está o time da Chapecoense. (Não jogando em 2025, use o Flamengo)"""

clubes = ('Palmeiras', 'Flamengo', 'Cruzeiro', 'Mirassol', 'Botafogo', 'Bahia', 'Fluminense',
          'São Paulo', 'Vasco da Gama', 'Bragantino', 'Ceará SC', 'Corinthians', 'Grêmio',
          'Atlético-MG', 'Internacional', 'Santos', 'EC Vitória', 'Fortaleza', 'Juventude',
          'Sport Recife')

print('=-=-'*15)
print('Lista de times do Brasileirão:')
for clube in clubes:
    print(f'  {clube}')

print('=-=-'*15)
print('Os 5 primeiros colocados são:')
for pos, clube in enumerate(clubes[:5]):
    print(f'{pos+1}º {clube}')

print('=-=-'*15)
print('Os 4 últimos colocados são')
for i in range(19, 15, -1):
    print(f'{i+1}º {clubes[i]}')

print('=-=-'*15)
print('Os times em ordem alfabética:')
for clube in sorted(clubes):
    print(f'  {clube}')

print('=-=-'*15)
print(f'O Flamengo está na {clubes.index('Flamengo')+1}ª posição')
