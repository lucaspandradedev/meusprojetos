print('-='*10,'DESAFIO DA P.A','=-'*10)
pt = int(input('Qual o primeiro termo da sua P.A?: '))
r = int(input('Qual a razão da sua P.A?: '))
for c in range(0,10):
    dpt = (pt + (r*c))
    print(dpt, end='>')