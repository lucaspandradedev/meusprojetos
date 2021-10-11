from time import sleep
from random import randint
numeros = []


def sorteia():
    for p in range(0, 5):
        num = randint(0, 10)
        numeros.append(num)
    print('Os valores sorteados são:', end=' ')
    for p in numeros:
        print('\033[1;31m', p, end=' -> ''\033[m')
        sleep(0.4)
    print('\033[1;31m''FIM!''\033[m')
    print(f'A lista gerada com esses números é: {numeros}')


def somapar():
    soma = c = 0
    while c < len(numeros):
        soma = c = 0
        for p in numeros:
            c += 1
            if p % 2 == 0:
                soma += p
    print(f'A soma de todos os valores pares da lista é {soma}')


sorteia()
somapar()
print('                      <<< FIM DO PROGRAMA >>>')
