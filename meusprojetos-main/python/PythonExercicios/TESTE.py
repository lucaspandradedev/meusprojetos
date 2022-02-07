def leiaFloat(txt):
    print(20 * '-')
    resp = float(input(txt))
    while True:
        if resp.isnumeric():
            r = resp
            return r
            break
        else:
            print('\033[1;31mERRO! Digite um número inteiro.''\033[m')
            resp = str(input(txt)).strip()


r = leiaFloat('Digite um número real: ')