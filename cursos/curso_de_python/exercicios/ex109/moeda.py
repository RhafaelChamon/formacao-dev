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
