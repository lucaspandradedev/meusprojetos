from time import sleep
def lin():
    print(30 * '=-')
def contador(a, b, c):
    print(f'Contador de {a} até {b} de {c.__abs__()} em {c.__abs__()}:')
    if c < 0:
        c *= -1
    if c == 0:
        c = 1
    if a < b:
        cont = a-c
        while cont < b:
            cont += c
            print(f'{cont}', end=' ')
            sleep(0.5)
        print('FIM !')
    else:
        cont = a+c
        while cont > b:
            cont -= c
            print(f'{cont}', end=' ')
            sleep(0.5)
        print('FIM !')


lin()
contador(1, 10, 1)
lin()
contador(10, 0, 2)
lin()
print('Agora é sua vez de personalizar a contagem!')
lin()
a = int(input('Início: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
contador(a, b, c)
lin()
print('                  <<< PROGRAMA ENCERRADO >>>')