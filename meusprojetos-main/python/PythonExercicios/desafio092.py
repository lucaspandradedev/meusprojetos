from datetime import datetime
dados = {}
while True:
    dados['Nome'] = str(input('Nome: ')).capitalize()
    ano = int(input('Ano de nascimento: '))
    dados['Idade'] = datetime.now().year - ano
    dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
    if dados['ctps'] == 0:
        break
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário R$: '))
    break
print(50*'-=')
print(dados)
for k,v in dados.items():
    print(f'O(A) {k} é {v}')
print(f'Esse trabalhador se aposentará com {(dados["Contratação"]+35)-ano} anos de idade')