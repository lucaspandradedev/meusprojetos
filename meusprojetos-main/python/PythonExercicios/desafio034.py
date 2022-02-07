s = float(input('Qual o salário do funcionário?: R$ '))
a1 = s * 1.15
a2 = s * 1.10
if s<=1250:
    print(f'O salário deste funcionário, com aumento de 15% é {a1:.2f}')
else:
    print(f'O salário desse funcionário, com aumento de 10% é {a2:.2f}')
