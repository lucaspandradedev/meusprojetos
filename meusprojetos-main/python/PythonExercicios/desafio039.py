from datetime import date
atual = date.today().year
an = int(input('Digite seu ano de nascimento: '))
qa = atual-an
tr = 18-qa
tp = qa-18
if qa<18:
    print('\033[1;32m''No momento, você não precisa se alista no serviço militar. Faltam {} ano(s) para seu alistamento'.format(tr))
elif qa == 18:
    print('\033[1;31m''Você deve se alistar no serviço militar ainda este ano!')
elif qa>18:
    print('\033[1;31m'f'Você está em dívida com o serviço militar. Já se passaram {tp} anos da data de alistamento')