print('Gerador de P.A')
pt = int(input('Digite o primeiro termo de sua P.A: '))
r = int(input('Digite a razão de sua P.A: '))
ct = 1
t = pt
while ct <= 10:
    print(t, end=' ➔ ')
    t += r
    ct += 1
print('FIM!\nEstes são os 10 primeiros termos da sua P.A!')




'''from time import sleep
print('       Gerador de P.A')
print('-=-'*10)
pt = int(input('Digite o primeiro termo de sua P.A: '))
r = int(input('Digite a razão de sua P.A: '))
c = 0
t = pt
s = r
print('Calculando os 10 primeiros termos da sua P.A...')
sleep(2)
while c < 10:
    print(t, end='')
    print(' > ' if c < 10 else ' ', end='')
    t += s
    c += 1
print('FIM') este foi o modo que fiz'''


'''fazer do jeito do professor depois'''
