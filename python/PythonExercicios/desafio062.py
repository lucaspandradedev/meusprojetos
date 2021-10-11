print('Gerador de P.A melhorado!')
pt = int(input('Digite o primeiro termo da sua P.A: '))
r = int(input('Digite a razão da sua P.A: '))
ct = 1
t = pt
total = 0
d = 10
while d != 0:
    total = total + d
    while ct <= total:
        print(t, end='')
        print(' ➔ ' if ct < 10 else ' ➔ ', end='')
        t += r
        ct += 1
    print('PAUSA')
    d = int(input('Quantos termos a mais você deseja mostrar? '))
print('FIM')
print(f'O total de termos mostrados foi de {total}')
















