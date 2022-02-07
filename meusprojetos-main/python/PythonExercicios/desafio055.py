maiorpeso = 0
menorpeso = 0
for c in range(1, 6):
    peso = float(input(f'Qual o peso da {c}ªpessoa?: '))
    if c == 1:
        maiorpeso = peso
        menorpeso = peso
    else:
        if peso > maiorpeso:
            maiorpeso = peso
        if peso < menorpeso:
            menorpeso = peso
print(f'O maior peso é {maiorpeso} kg')
print(f'O menor peso é {menorpeso} kg')










'''lista = []
for c in range (1,6):
    lista.append(float(input (f'Qual o peso da {c}ª pessoa?: ')))
m = max(lista)
mi = min(lista)
print (f'O maior peso é {m}kg')
print (f'O menor peso é {mi}kg')'''











'''''maior = 0
menor = 0
for c in range(1,6):
    p = float(input(f'Qual o peso da {c}ª pessoa?: '))
    if p == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p
print(f'O maior peso lido foi de {maior} kg')
print(f'O menor peso lido foi de {menor} kg')'''''
