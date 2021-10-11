d = int(input('Quantos dias você alugou? '))
s = float(input('Quantos km você rodou? '))
v = (60*d) + (0.15*s)
print('O valor a ser pago será: {} R$'.format(v))
