dados = {}
gols = []
listadados = []
while True:
    print(40*'-')
    gols.clear()
    dados['Nome'] = str(input('Nome do jogador: ')).capitalize()
    np = int(input(f'Quantas partidas {dados["Nome"]} jogou?: '))
    for p in range(1, np+1):
        ng = int(input(f'Quantos gols fez na partida {p}?: '))
        gols.append(ng)
        dados['Gols'] = gols[:]
        dados['Total de Gols'] = sum(gols)
    listadados.append(dados.copy())
    resp = str(input('Deseja continuar [S/N]?: ')).upper().strip()
    if resp == 'N':
        break
print(40*'=-')
print(listadados)
print(f'{"Cod.":<5}{"Nome":<8}{"Gols":<15}{"Total":<20}')
for p,i in enumerate(listadados):
    print(f'{p:<5}{i["Nome"]:<8}{str(i["Gols"]):<15}{i["Total de Gols"]:<20}')
while True:
    mostr = int(input('Mostrar dados de qual jogador? (999 para encerrar): '))
    if mostr == 999:
        break
    if mostr >= len(listadados):
        print('ERRO! Não existe jogador nessa posição!')
    else:
        print(f'   --- LEVANTAMENTO DO JOGADOR {listadados[mostr]["Nome"].upper()} ---')
        for i,g in enumerate(listadados[mostr]['Gols']):
            print(f'            No jogo {i+1} fez {g} gols')

print('<<< ENCERRANDO >>>')



