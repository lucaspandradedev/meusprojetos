peso = float(input('Qual o seu peso?: '+'kg'))
alt = float(input('Qual a sua altura?: '+'m'))
imc = (peso)/(alt**2)
if imc < 18.5:
    print('\033[1;33m Você está abaixo do peso ideal!')
elif 18.5 < imc < 25:
    print('\033[1;4;36m Você está no seu peso ideal, parabéns!')
elif 25 <= imc <= 30:
    print('\033[1;31m Cuidado, você está com sobrepeso!')
elif 30 <= imc <= 40:
    print('\033[1;31m Muito cuidado! Você se encontra em condição de obesidade!')
else:
    print('\033[1;4;31m Você está em condição de obesidade mórbida! Procure um médico o mais rápido possível!')