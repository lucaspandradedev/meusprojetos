from random import randint
n1 = randint(0,10)
n2 = randint(0,10)
n3 = randint(0,10)
n4 = randint(0,10)
n5 = randint(0,10)
t = (n1,n2,n3,n4,n5)
tc = sorted(t)
print(f'Os números sorteados foram {t}')
print(f'O valor máximo foi {tc[4]}')
print(f'O valor mínimo foi {tc[0]}')

#aqui eu poderia ter formado uma tupla só, colocando o randint dentro da própria tupla, assim: ((randint(0,10),...
#ao invés de colocar em ordem crescente, eu poderia usar somento as funções de max e min