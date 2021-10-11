'''jeito do professor'''
n = int(input('Digite um número para saber seu fatorial: '))
c = n
f = 1
print(f'Calculando {n}!',end=' >> ')
while c > 0:
    print(f'{c}',end=' ')
    print('x ' if c > 1 else '= ', end='')
    f *= c
    c -= 1
print(f'{f}')




'''n = int(input('Digite um número: '))
resultado = 1
contador = 1
while contador <= n:
    resultado = resultado * contador
    contador += 1
print(f'O fatorial desse número é {resultado}')'''
