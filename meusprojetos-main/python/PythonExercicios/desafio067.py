while True:
    v = int(input('De qual número deseja saber a tabuada?: '))
    print(15 * '-*-')
    if v < 0:
        break
    for c in range(1,11):
        print(f'{v} x {c} = {v*c}')
    print(15*'-*-')
print('\033[1;4;34m''FIM DO PROGRAMA TABUADA!')






'''while True:
    v = int(input('Quer ver a tabuada de que valor?: '))
    if v < 0:
        break
    print(15*'=')
    print(f'{v} x {1} = {v * 1}', end='\n')
    print(f'{v} x {2} = {v * 2}', end='\n')
    print(f'{v} x {3} = {v * 3}', end='\n')
    print(f'{v} x {4} = {v * 4}', end='\n')
    print(f'{v} x {5} = {v * 5}', end='\n')
    print(f'{v} x {6} = {v * 6}', end='\n')
    print(f'{v} x {7} = {v * 7}', end='\n')
    print(f'{v} x {8} = {v * 8}', end='\n')
    print(f'{v} x {9} = {v * 9}', end='\n')
    print(f'{v} x {10} = {v * 10}', end='\n')
    print(15*'=')
print('PROGRAMA TABUADA ENCERRADO!')'''




