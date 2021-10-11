dados = {}
gols = []
dados['Nome'] = str(input('Qual o nome do jogador?: ')).capitalize()
nj = int(input(f'Quantas partidas {dados["Nome"]} jogou?: '))
for p in range(0, nj):
     n = int(input(f'Quantos gols na partida {p}?: '))
     gols.append(n)
     dados['Gols'] = gols
     dados['Total de Gols'] = sum(gols)
print(40*'-=')
print(dados)
for k,v in dados.items():
    print(f'O campo {k} tem valor {v}')
print(40*'=')
print(f'O jogador {dados["Nome"]} jogou {nj} partidas')
#no lugar  do for, que eu usei, o professor usou o for i,v enumerate(jogador['Gols']) com f' {i} e {v}
for p in range(0, nj):
    print(f'=> Na partida {p}, fez {gols[p]} gols.')
print(f'Foi um total de {sum(gols)} gols.')

