"""Exercício Python 97: Faça um programa que tenha uma função chamada
   escreva(), que receba um texto qualquer como parâmetro e mostre uma
   mensagem com tamanho adaptável."""

def escreva(txt):
    print('~' * (len(txt) + 4))
    print(f'{txt:^{len(txt) + 4}}')
    print('~' * (len(txt) + 4))


escreva('Python')
escreva('#Dev2026')
escreva('#AprendendoPython')
