def leiaInt(txt):
    print(20 * '-')
    resp = str(input(txt)).strip()
    while True:
        if resp.isnumeric():
            n = resp
            return n
            break
        else:
            print('\033[1;31mERRO! Digite um número inteiro.''\033[m')
            resp = str(input(txt)).strip()

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')

#outro código para função(do professor):
'''ok = False
    valor = 0
    while True:
        n = str(input(txt))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[1;31mERRO! Digite um número inteiro.''\033[m')
        if ok:
            break
    return valor'''