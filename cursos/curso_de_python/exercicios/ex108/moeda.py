def aumentar(x, valor):
    x += x * valor /100
    return x


def diminuir(x, valor):
    x -= x * valor /100
    return x


def dobro(x):
    x *= 2
    return x


def metade(x):
    x /= 2
    return x


def moeda(x):
    return f'R${x:.2f}'.replace('.', ',')
