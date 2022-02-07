from time import sleep
from random import randint
'''def maior(list):
    list = []
    for p in range(0, randint(0, 10)):
        valor = randint(0, p)
        list.append(valor)
    print(30*'-=')
    print('Analisando os valores recebidos....')
    sleep(1)
    for p in list:
        print(p, end=' -> ')
        sleep(0.4)
    if len(list) == 0:
        print('NENHUM VALOR FOI INFORMADO')
    if len(list) > 0:
        print(f'Foram informados {len(list)} valores ao todo')
        print(f'O maior valor informado foi {max(list)}')

    
for p in range(0,randint(0,10)):
    maior(list)
print(30*'-=')
print('             <<< ENCERRADO O PROGRAMA >>>')'''   #foi como eu fiz

def maior(* num):
    cont = maior = 0
    print(30 * '-=')
    print('Analisando os valores recebidos...')
    for valor in num:
        print(valor, end=' ')
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print()
    print(f'Foram informados ao todo {cont} valores')
    print(f'O maior valor é {maior}')




maior(1,5,2,10,12,19,0)
maior(1,5,2,8,7)
maior(1,5,9,3,6,9,7)
maior(7,3,9,15,10,25,23,19)