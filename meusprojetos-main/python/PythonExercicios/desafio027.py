nome = str(input('Digite seu nome completo: ')).strip()
s = nome.split()
p = s[0]
u = s.reverse()
print(f'Seu primeiro nome é {p}')
print(f'Seu último nome é {s[0]}')
#print(f'Seu ultimo nome é {len(s)}')
print(s)

''' o professor utilizou para o ultimo nome a função len(s)-1'''