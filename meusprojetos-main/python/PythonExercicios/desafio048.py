soma = 0
for c in range(1,501,2):
    if c % 3 == 0:
        np = c
        soma = soma + np
print(f'A soma de todos os números ímpares que são múltiplos de três, no intervalo de 1 à 501 é {soma}')