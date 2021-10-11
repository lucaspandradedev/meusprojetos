import random
n = random.randint(0,9999)
p = n % 2
print(n)
if p == 0:
    print('PAR')
else:
    print('IMPAR')