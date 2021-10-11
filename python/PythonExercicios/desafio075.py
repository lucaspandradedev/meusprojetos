n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))
t = (n1,n2,n3,n4)
print(t)
print(f'O número 9 (nove) apareceu {t.count(9)} vezes')
if 3 in t:
    print(f'O número 3(três) aparece na {t.index(3)+1}ª posição')
else:
    print('O número 3(três) não aparece em posição alguma')
print('Os valores pares digitados foram: ',end='')
for c in t:
    if c % 2 == 0:
        print(c,end=' ')


