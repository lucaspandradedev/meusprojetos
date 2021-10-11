'''dados = []
dic = {}
mulheres = []
contp = somaid = 0
while True:
    dic['Nome'] = str(input('Nome: ')).capitalize()
    contp += 1
    dic['Idade'] = int(input('Idade: '))
    somaid += dic['Idade']
    dic['Sexo'] = str(input('Sexo: ')).upper()
    if dic['Sexo'] == 'F':
        mulheres.append(dic['Nome'])
    dados.append(dic.copy())
    de = str(input('Deseja continuar [S/N]?: ')).strip().upper()
    while de not in 'SN':
        print('Opção inválida, tente novamente com S ou N')
        de = str(input('Deseja continuar [S/N]?: ')).strip().upper()
    if de == 'N':
        break
print(dados)
print(f'-> O total de pessaos cadastradas foram: {contp}')
print(f'-> A média de idade do grupo foi de: {somaid/contp} anos')
print(f'-> As mulheres cadastradas foram: {mulheres}')
print('-> Lista de pessoas que estão acima da média:')
for p in range(0, len(dados)):
    if dados[p]['Idade'] > (somaid/contp):
        print(f'Nome - {dados[p]["Nome"]:},  Sexo - {dados[p]["Sexo"]:},  Idade - {dados[p]["Idade"]:}')
print('FINALIZANDO...')
sleep(1)
print('<<< ENCERRADO >>>')'''


galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: ')).capitalize()
    while True:
        pessoa['Sexo'] = str(input('Sexo [M/F]:? ')).upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print(galera)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas')
print(f'B) A média de idades é de {soma/len(galera):5.2f} anos')
print('C) As mulheres cadastradas foram', end=' ')
for p in galera:
    if p['Sexo'] in 'Ff':
        print(p['Nome'], end='')
print(f'D) Lista de pessoas que estão acima da média:', end='')
for p in galera:
    if p['Idade'] >= media:
        print('   ')
        for k,v in p.items():
            print(f'{k} = {v} ; ', end='')
        print()