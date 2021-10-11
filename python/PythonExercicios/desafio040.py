n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
me = (n1+n2)/2
if me<5.0:
    print('\033[1;4;31m''REPROVADO')
elif 5.0<me<6.9:
    print('\033[1;4;33m''RECUPERAÇÃO')
else:
    print('\033[1;4;32m''APROVADO')