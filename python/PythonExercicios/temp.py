
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