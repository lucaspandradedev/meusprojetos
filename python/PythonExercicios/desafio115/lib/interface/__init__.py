'''def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInt('Sua opção: ')
    return opc'''


def linha(tam=42):
    return tam * '-'

def head(txt):
    print(50*'-')
    print(f'{txt}'.center(50))
    print(50 * '-')
    print('1 - \033[34mVer pessoas cadastradas''\033[m')
    print('2 - \033[34mCadastrar novas pessoas''\033[m')
    print('3 - \033[34mSair do sistema''\033[m')
    print(50 * '-')


def opc():
    resp = [1, 2, 3]
    while True:
        try:
            cho = resp[int(input('\033[33mQual sua opção?: ''\033[m'))-1]
        except IndexError:
            print('\033[1;31mERRO! Por favor, digite uma das oções válidas.''\033[m')
        except (ValueError,TypeError):
            print('\033[1;31mERRO! Digite uma das opções válidas.''\033[m')
        else:
            return cho


def opc1(txt):
    print(50 * '-')
    print(f'{txt}'.center(50))
    print(50 * '-')


