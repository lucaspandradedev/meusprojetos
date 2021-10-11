import random
a = input('Aluno 1: ')
b = input('Aluno 2: ')
c = input('Aluno 3: ')
d = input('Aluno 4: ')
l = [a,b,c,d]
s = random.sample(l,4)
print(f'A ordem de apresentação foi, respectivamente: {s}')
