n1 = int(input('Digite um número '))
n2 = int(input('Digite outro número '))
s = n1+ n2
cor = {'limpa':'\033[m',
       'azul':'\033[1;34m',
       'verm':'\033[1;31m'}
print(f'A soma entre \033[1;34m{n1}\033[m e \033[1;34m{n2}\033[m,vale \033[1;31m{s}')
