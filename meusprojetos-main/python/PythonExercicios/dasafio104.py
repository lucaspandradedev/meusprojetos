'''def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[1;31mERRO! Digite um número inteiro válido!''\033[m')
        if ok:
            break
    return valor''' #foi assim que o professor fez


def leiaInt(n):
    p = input('Digite um número: ')
    if p.isnumeric():
        return p
    while p.isalpha() or p.isalnum() or p.isspace() or p.strip() == '' or p.isalnum():
        print('\033[1;31m''ERRO! O valor digitado não é um número inteiro!''\033[m')
        p = input('Digite um número: ')
        if p.isnumeric():
            return p


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
