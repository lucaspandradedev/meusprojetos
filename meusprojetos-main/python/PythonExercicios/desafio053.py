frase = str(input("Digite uma frase: ")).upper()
junto = frase.replace(" ","")
i = junto[::-1]
print(f'O inverso dessa frase é: {i}')
if junto == i:
    print("Esta frase é um palíndromo")
else:
    print("Esta frase não é um palíndromo")




"""print("Sua frase é: "+ re)"""
