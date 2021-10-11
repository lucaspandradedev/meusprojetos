def ficha(nome='<Desconhecido>',gols=0):
   print(f'O jogador {nome.capitalize()} fez {gols} gol(s) no campeonato')


print(30*'-')
n = str(input('Nome do jogador: '))
g = str(input('Números de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)