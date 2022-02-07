def leiaInt(txt):
    print(30 * '-')
    while True:
        try:
            resp = int(input(txt))
        except (ValueError,TypeError):
            print('\033[1;31mERRO! Digite um número inteiro.''\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[1;31mO usuário preferiu não digitar um valor.''\033[m')
            return 0
        else:
            return resp

def leiaFloat(txt):
    while True:
        try:
            resp = float(input(txt))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite um número real.''\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[1;31mO usuário preferiu não digitar um valor.''\033[m')
            return 0
        else:
            return resp


i = leiaInt('Digite um número inteiro: ')
r = leiaFloat('Digite um número real: ')
print(f'O número inteiro digitado foi {i}')
print(f'O número real digitado foi {r}')




