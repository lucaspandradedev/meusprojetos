from time import sleep
vc = int(input('Qual o valor da casa?: R$'))
s = int(input('Qual o seu salário?: R$'))
p = int(input('Em quantos anos pretende pagar esse valor?: '))
vp = vc/p
print('\033[1;34m' 'ANALISANDO...')
sleep(2)
if vp>(0.3 * s):
    print('\033[1;31m''FINANCIAMENTO NEGADO!!!')
elif vp == (0.3 * s):
    print('\033[1;32m''FINANCIAMENTO APROVADO!!!')
else:
    print('\033[1;32m''FINANCIAMENTO APROVADO!!!')
