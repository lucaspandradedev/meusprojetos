n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))
if n1>n2 and n1>n3:
    print(f'O maior valor entre os três é o {n1}')
if n2>n1 and n2>n3:
    print(f'O maior valor entre os três é o {n2}')
if n3>n2 and n3>n1:
    print(f'O maior valor entre os três é o {n3}')
if n1<n2 and n1<n3:
    print(f'O menor valor entre os três é o {n1}')
if n2<n1 and n1<n3:
    print(f'O menor valor entre os três é o {n2}')
if n3<n2 and n3<n1:
    print(f'O menor valor entre os três é o {n3}')

'''A sugestão do professor é fixar um dos números. Por exemplo, se o menor for "a", então eu tenho que se b<a e b<c
então b é o menor de todos e assim por diante. Já para o maior, segue do mesmo jeito, fixamos "a" como maior e se b>a
e b>c, então b é o maior'''