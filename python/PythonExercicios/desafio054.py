cont = 0
contt = 0
for c in range(0,7):
    an = int(input("Digite o ano de seu nascimento: "))
    if an <= 2003:
        cont += 1
    elif an > 2003:
        contt += 1
print(f"O número de pessoas menores de idade é {contt}")
print(f"O número de pessoas maiores de idade é {cont}")