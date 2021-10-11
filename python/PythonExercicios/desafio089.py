print(5*'<','BOLETIM DOS ALUNOS',5*'>')
dados = []
dadost = []
while True:
    nome = str(input('Nome: ')).capitalize()
    nt1 = float(input('Nota 1: '))
    nt2 = float(input('Nota 2: '))
    med = (nt1+nt2)/2
    dadost.append(nome)
    dadost.append(nt1)
    dadost.append(nt2)
    dadost.append(med)
    dados.append(dadost[:])
    dadost.clear()
    dec = str(input('Deseja continuar cadastrando no boletim [S/N]?: ')).strip().upper()
    while dec not in 'NS':
        dec = str(input('Deseja continuar cadastrando no boletim [S/N]?: ')).strip().upper()
    if dec == 'N':
        break
print(40*'-=')
print(30*'-')
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>10}')
for i,p in enumerate(dados):
    print(f'{i:<4}{p[0]:<10}{p[3]:>10}')
print(30*'-')
while True:
    mn = int(input('Mostrar notas de qual aluno(a)? (999 para interromper): '))
    if mn == 999:
        break
    print(f'As notas de {dados[mn][0]} são {dados[mn][1:3]}')
print('FINALIZANDO...\n<<< VOLTE SEMPRE >>>')


#algumas alterações do professor
'''print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
for i,p in enumerate(dados):
    print(f'{i}   {p[0]:>5}{p[3]:>18}')
print(30*'-')
while True:
    mn = int(input('Mostrar notas de qual aluno(a)? (999 para interromper): '))
    if mn == 999:
        break
    for i, p in enumerate(dados):
        print(f'As notas de {p[mn]} são {p[1:3]}')
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha [opc][0] são {cad[opc][1]'}
print('FINALIZANDO...\n<<< VOLTE SEMPRE >>>')'''
