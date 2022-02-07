name = str(input('Digite seu nome '))
nss = name.replace(' ','')
nd = name.split()
print(f'Seu nome em maiúsculas é {name.upper()}')
print(f'Seu nome em minusculas é {name.lower()}')
print(f'Seu nome tem ao todo {len(nss)} letras')
print(f'Seu primeiro nome tem {len(nd[0])} letras')



#print(f'Seu primeiro nome tem {name.find(" ")} letras')
#print(f'Seu nome tem ao todo {len(name)-name.count(" ")} letras')