from random import randint
from time import sleep
print(40*'=')
print(11*' '+'JOGA NA MEGA SENA')
print(40*'=')
nj = int(input('Quantos jogos você quer que eu sorteie? '))
print(5*'=-',f'<< SORTEANDO {nj} JOGO(S) >>',5*'-=')
listajogo = []
for n in range(1, nj+1):
    for c in range(0,6):
        num = randint(1,60)
        if num in listajogo:
            num = randint(1, 60)
            listajogo.append(num)
        else:
            listajogo.append(num)
    sleep(1)
    print(f'Jogo {n}: {sorted(listajogo)}')
    listajogo.clear()
print(7*'-=','<< BOA SORTE! >>',7*'=-')


'''lista = list()    #foi como o professor fez
jogos = list()
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'SORTEANDO {quant} JOGOS')
for i,l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('BOA SORTE!')'''