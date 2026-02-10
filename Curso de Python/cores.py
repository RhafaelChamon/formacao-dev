print('Formato: \033[1:30:42m{:^20}\033[m\n'.format(r'\033[1:30:42m'))
print('{:^20}'.format('None'))
print('\033[::40m{:^20}\033[m'.format('0')) # Preto
print('\033[::41m{:^20}\033[m'.format('1')) # Vermelho
print('\033[::42m{:^20}\033[m'.format('2')) # Verde
print('\033[::43m{:^20}\033[m'.format('3')) # Amarelo
print('\033[::44m{:^20}\033[m'.format('4')) # Azul
print('\033[::45m{:^20}\033[m'.format('5')) # Roxo
print('\033[::46m{:^20}\033[m'.format('6')) # Ciano
print('\033[::47m{:^20}\033[m'.format('7')) # Cinza
print('\033[4m{}\033[m\n'.format(' '*30))
print('\033[m{:^20}\033[m'.format('None'))
print('\033[0m{:^20}\033[m'.format('0 = Normal'))
print('\033[1m{:^20}\033[m'.format('1 = Negrito'))
print('\033[4m{:^20}\033[m'.format('4 = Sublinhado'))
print('\033[7m{:^20}\033[m'.format('7 = Inverter Cores'))
