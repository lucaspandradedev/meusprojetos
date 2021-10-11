n = int(input('Digite um número: '))
'''print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena {c}')
print(f'Milhar: {m}')'''
'''print(f'Unidade: {d[0][3]}')
print(f'Dezena: {d[0][2]}')
print(f'Centena: {d[0][1]}')
print(f'Milhar: {d[0][0]}')'''
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')
