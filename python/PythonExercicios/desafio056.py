chmaior = 0
cmmenor = 0
idadehmv = 0
somaidade = 0
for c in range(1, 5):
    nome = str(input(f'Qual o nome da {c}ª pessoa? '))
    idade = int(input(f'Qual a idade da {c}ª pessoa? '))
    sexo = str(input(f'Qual o sexo da {c}ª pessoa? [M/F]? '))
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        idadehmv = idade
        chmaior = nome
    if sexo in 'Mm' and idade > idadehmv:
        idadehmv = idade
        chmaior = nome
    if sexo in "Ff" and idade < 20:
        cmmenor += 1
print(f'A média de idade dessas 4 pessoas é {somaidade/4}')
print(f'O homem mais velho tem {idadehmv} anos e se chama {chmaior}')
print(f'Há {cmmenor} mulheres abaixo dos 20 anos')
