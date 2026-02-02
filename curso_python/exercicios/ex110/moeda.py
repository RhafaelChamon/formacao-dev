def aumentar(x, valor, format_real=True):
    x += x * valor /100
    if format_real:
        return moeda(x)
    else:
        return x


def diminuir(x, valor, format_real=True):
    x -= x * valor /100
    if format_real:
        return moeda(x)
    else:
        return x


def dobro(x, format_real=True):
    x *= 2
    if format_real:
        return moeda(x)
    else:
        return x


def metade(x, format_real=True):
    x /= 2
    if format_real:
        return moeda(x)
    else:
        return x


def moeda(x):
    return f'R${x:.2f}'.replace('.', ',')


def resumo(x, aum, dim):
    print('-' * 30)
    print(f'{"Resumo do valor":^30}')
    print('-' * 30)
    print(f'{"Preço analisado:":<20}{moeda(x)}')
    print(f'{"Dobro do preço:":<20}{dobro(x)}')
    print(f'{"Metade do preço:":<20}{metade(x)}')
    print(f'{f"{aum}% de aumento:":<20}{aumentar(x, aum)}')
    print(f'{f"{dim}% de redução:":<20}{diminuir(x, dim)}')
