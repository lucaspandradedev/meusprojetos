import random
v = random.randint(20,120)
m = (v-80)*7
print(f'Valor da velocidade registrado: {v} km/h')
if v>80:
    print(f'Você está em excesso de velocidade. Será multado em {m} reais')
else:
    print('Parabéns, você está dentro dos limites de velocidade!')