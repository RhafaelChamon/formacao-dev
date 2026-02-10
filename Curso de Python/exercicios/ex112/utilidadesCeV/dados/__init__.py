def leiadinheiro(msg):
    while True:
        ent = input(msg).strip().replace(',', '.')
        try:
            ent = float(ent)
            return ent
        except ValueError:
            print(f'\033[1:31mINVÁLIDO!\033[m '
                  f'"{ent}" não é um preço válido. Tente novamente.')
