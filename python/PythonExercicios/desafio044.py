from time import sleep
pn = float(input('Qual o preço do produto?: R$ '))
print('Você pode escolher pagar das seguintes formas:\n1-À vista no dinheiro/cheque;\n2-À vista no cartão;\n3-Em até 2x vezes no cartão;\n4-Em até 3x ou mais no cartão. ')
mp = int(input('Qual das formas listadas se encaixa melhor no seu orçamento?: '))
print('\033[1;32mCALCULANDO PREÇO...')
sleep(2)
if mp == 1:
    print(f'O valor a ser pago será de R$ \033[1;34m{pn*0.90}')
elif mp == 2:
    print(f'O valor a ser pago será de R$ \033[1;34m{pn*0.95}')
elif mp == 3:
    print(f'O valor a ser pago será de R$ \033[1;34m{pn}')
else:
    print(f'O valor a ser pago será de R$ \033[1;34m{pn*1.20}')