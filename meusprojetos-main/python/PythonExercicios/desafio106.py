from time import sleep


def ini(txt):
    tam = len(txt) + 4
    print('\033[1;42m',end='')
    print(tam * '~')
    print(f'  {txt}')
    print(tam * '~')
    print('\033[m', end='')


def acess(txt):
    tam = len(txt) + 4
    print('\033[1;46m',end='')
    print(tam * '~')
    print(f'  {txt}')
    print(tam * '~')
    print( '\033[m',end='')


def dica(ajuda):
    return ajuda


def fim(txt):
    tam = len(txt) + 4
    print('\033[1;41m', end='')
    print(tam * '~')
    print(f'  {txt}')
    print(tam * '~')
    print('\033[m', end='')


while True:
    ini('SISTEMA DE AJUDA PyHELP')
    ajuda = str(input('Função ou Biblioteca > '))
    if ajuda.lower() == 'fim':
        break
    acess(f'Acessando o manual do comando "{ajuda}"')
    sleep(1)
    print('\033[7;40m')
    help(ajuda)
    print('\033[m',end='')
    sleep(1)
fim('ATÉ LOGO!')
