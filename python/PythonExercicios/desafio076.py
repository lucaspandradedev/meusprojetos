listagem = ('Maça',1.50,'Banana',2.00,'Geleia',10.00,'Nutella',20.00)
print(50*'-')
print(f'{"LISTAGEM DE PREÇOS":^48}')
print(50*'-')
for pos in range(0,len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end=' R$ ')
    else:
        print(f'{listagem[pos]:.2f}')
print(50*'-')
# e foi assim que o professor fez!

















'''t = ('Maça',1.50,'Banana',2.00,'Geleia',10.00,'Nutella',20.00)
print(50*'-')
print(15*' '+'LISTAGEM DE PREÇOS')
print(50*'-')
print(t[0],'..................... R$',t[1])
print(t[2],'..................... R$',t[3])
print(t[4],'..................... R$',t[5])
print(t[6],'..................... R$',t[7]) foi como eu fiz'''
