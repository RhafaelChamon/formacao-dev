from pathlib import Path


def linha_d(tam=80):
    return '=' * tam


def titulo(msg, tam=80):
    if tam < len(msg):
        tam = len(msg) + 2
    print(linha_d(tam))
    print(f'|{msg:^{tam-2}}|')
    print(linha_d(tam))


def menu(opcoes):
    titulo('MENU PRINCIPAL')
    for i, opc in enumerate(opcoes):
        print(f'\033[33m[{i+1}]\033[m \033[34m{opc}\033[m')
    while True:
        try:
            n = int(input(f'{"-"*15} \033[36mSua opção: \033[m'))
            if 1 <= n <= len(opcoes):
                return n
            else:
                print(f'\033[31mOpção inválida!\033[m Tente novamente.')
        except KeyboardInterrupt:
            print(f'\n\033[31mERROR: <KeyboardInterrupt>.\033[m Usuário forçou a parada do programa.')
            return 3
        except Exception as error:
            print(f'\033[31mERROR: {error.__class__}.\033[m Tente novamente.')


def exist_cadastros():
    p = Path('cadastros.txt')
    if not p.exists():
        Path('cadastros.txt').touch()


def list_pessoas():
    titulo('PESSOAS CADASTRADAS')
    p = Path('cadastros.txt')
    lista = p.read_text(encoding='utf-8').split('\n')
    form_nome = 30
    form_idade = 2
    for i in range (0, len(lista)):
        lista[i] = lista[i].split('#')
        try:
            if len(lista[i][0]) > form_nome:
                form_nome = len(lista[i][0])
            if len(lista[i][1]) > form_idade:
                form_idade = len(lista[i][1])
        except IndexError:
            continue
    print(f'{"Nome":<{form_nome}}   {"Idade"}')
    print(f'{"-" * form_nome}---{"-" * form_idade}-----')
    for k in lista:
        try:
            print(f'{k[0]:<{form_nome}}   {k[1]:>{form_idade}} anos')
        except IndexError:
            continue
    print('\n')


def sair():
    titulo('SAINDO DO PROGRAMA... Até logo!')


def leia_idade(msg):
    while True:
        try:
            valor = int(input(msg))
            return str(valor)
        except (ValueError, TypeError) as erro:
            print(f'\033[1:31mERRO: {erro.__class__}.\033[m Digite uma idade válida.')
        except KeyboardInterrupt as erro:
            print(f'\n\033[1:31mERRO: {erro.__class__}.\033[m O usuário não digitou a idade.')
            return None


def leia_nome(msg):
    while True:
        try:
            palavra = input(msg).strip().title()
            if palavra: return palavra
            else: print(f'\033[31mDigite um nome!\033[m')
        except KeyboardInterrupt as erro:
            print(f'\n\033[1:31mERRO: {erro.__class__}.\033[m O usuário não digitou o nome.')
            return None


def cadastrar_pessoa():
    titulo('NOVO CADASTRO')
    p = Path('cadastros.txt')
    nome = leia_nome('Nome: ')
    idade = leia_idade('Idade: ')
    if nome and idade:
        with p.open('a', encoding='utf-8') as f:
            if p.read_text(encoding='utf-8'):
                f.write(f'\n{nome}#{idade}')
            else:
                f.write(f'{nome}#{idade}')
        print(f'{nome} foi cadastrado(a) com sucesso!\n\n')
    else:
        print(f'Cadastro cancelado.\n\n')
