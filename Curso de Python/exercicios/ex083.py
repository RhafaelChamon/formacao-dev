"""Exercício Python 83: Crie um programa onde o usuário digite uma expressão
   qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão
   passada está com os parênteses abertos e fechados na ordem correta."""

paren = []
exp = input('Digite uma expressão numérica com parênteses: ')
exp_fatiada = list(exp)
for i in exp_fatiada:
    if i == '(':
        paren.append(i)
    elif i == ')':
        if len(paren) > 0:
            paren.pop()
        else:
            paren.append(i)
            break
if len(paren) == 0:
    print('A expressão está correta')
else:
    print('A expressão não está correta')
