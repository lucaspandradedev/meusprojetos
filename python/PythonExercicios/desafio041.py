ano = int(input('Digite seu ano de nascimento: '))
idat = 2021 - ano
if idat<=9:
    print('\033[1;34m''CATEGORIA MIRIM')
elif 9<idat and idat <= 14:
    print('\033[1;34m''CATEGORIA INFANTIL')
elif 14 < idat and idat <= 19:
    print('\033[1;34m''CATEGORIA JUNIOR')
elif 19 < idat and idat <= 20:
    print('\033[1;34m''CATEGORIA SÊNIOR')
else:
    print('\033[1;34m''CATEGORIA MASTER')
