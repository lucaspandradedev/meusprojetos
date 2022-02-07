print(10 * '*-*-')
print('      Sequencia de Fibonacci')
print(10 * '=-=-')
n = int(input('Quantos números deseja mostrar na sequencia? '))
t1 = 0
t2 = 1
t3 = t1 + t2
t = 0
print(f'{t1} ➔ {t2}', end=' ➔ ')
c = 3
while c <= n:
    t3 = t1 + t2
    print(t3, end=' ➔ ')
    t1 = t2
    t2 = t3
    c += 1
print('FIM')
