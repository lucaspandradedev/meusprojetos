dados = {}
dados['Nome'] = str(input('Nome do aluno: ')).capitalize()
dados['Média'] = float(input(f'Média de {dados["Nome"]}: '))
if dados["Média"] >= 7:
    dados['Situação'] = 'Aprovado'
elif 5 < dados["Média"] < 7:
    dados['Situação'] = 'Recuperação'
else:
    dados['Situação'] = 'Reprovado'
for k,v in dados.items():
    print(f'{k} é igual a {v}')