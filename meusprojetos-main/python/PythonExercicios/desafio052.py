n = int(input('Digite um número: '))
if n == 1:
    print("Este não é um número primo!")
elif n == 2:
    print("Esté é um número primo")
elif n % 1 == 0 and n % n == 0 and n % 2 != 0:
    print('Este é um número primo!')
else:
    print("Este não é um número primo")
