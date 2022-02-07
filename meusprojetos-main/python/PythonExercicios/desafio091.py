from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogador1': randint(1,6),
        'Jogador2': randint(1,6),
        'Jogador3': randint(1,6),
        'Jogador4': randint(1,6)}
ranking = {}
print('Valores sorteados:')
for v,k in jogo.items():
    print(f'{v} tirou {k}')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(40*'-=')
print('      =-= RANK DOS JOGADORES =-=')
for v,k in enumerate(ranking):
    print(f'  {v+1}º lugar {k[0]} tirou {k[1]} no dado')
    sleep(1)

# JEITO DO PROFESSOR ACIMA


'''dados = {}
cla = []
dados['Jogador'] = 'Jogador1','Jogador2','Jogador3','Jogador4'
for n in range(0,4):
    dados['Resultado'] = randint(1,6),randint(1,6),randint(1,6),randint(1,6)
cla.append(dados['Resultado'])
cla.sort()
print(cla)
print(dados)'''