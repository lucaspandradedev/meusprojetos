pessoas = []
dados = []
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    if len(pessoas) >= 1:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    re = input('Deseja continuar cadastrando [S/N]?: ').strip().upper()
    if re not in 'SN':
        print('Resposta inválida, tente novamente!')
        re = input('Deseja continuar cadastrando [S/N]?: ')
    if re == 'N':
        break
print(f'Os dados foram {pessoas}')
print(f'A quantidade de pessoas cadastradas foi {len(pessoas)}')
print(f'O maior peso foi de {maior} Kg. As pessoas com esse peso são: ', end='')
for c in pessoas:
    if c[1] == maior:
        print(f'[{c[0]}]', end='')
print( )
print(f'O menor peso foi de {menor} Kg. As pessoas com esse peso são: ', end='')
for c in pessoas:
    if c[1] == menor:
        print(f'[{c[0]}]', end='')



