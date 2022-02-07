d = int(input('Qual a distância total do percurso da sua viagem, em km?: '))
p1 = 0.50 * d
p2 = 0.45 * d
if d<=200:
    print(f'O valor da sua viagem será de R$ {p1} ')
else:
    print(f'O valor da sua viagem será de R$ {p2}')