listan = []
for c in range(0, 5):
    n = int(input('Digite um número: '))
    if c == 0 or n > listan[-1]:
        listan.append(n)
    else:
        pos = 0
        while pos < len(listan):
            if n <= listan[pos]:
                listan.insert(pos, n)
                break
                pos += 1
print(40*'=')
print(f'Os valores digitados, na ordem crescente, foram {listan}')
#parece que esse código está bugado; talvez seja alguma coisa com o pycharm








''''listan = []
c = 0
while True:
    n = int(input('Digite um número: '))
    c += 1
    if c == 1:
        listan.append(n)
    if c == 2:
        if n < max(listan):
            listan.insert(0,n)
        else:
            listan.insert(1,n)
    if c == 3:
        if min(listan) < n < max(listan):
            listan.insert(1,n)
    if c == 4:
        if min(listan) < n < listan[1]:
            listan.insert(1,n)
        if listan[1] < n < max(listan):
            listan.insert(2,n)
    if c == 5:
        if min(listan) < n < listan[1]:
            listan.insert(1,n)
        if listan[2] < n < max(listan):
            listan.insert(3,n)
        if n < min(listan):
            listan.insert(0,n)
        if n > max(listan):
            listan.insert(4,n)
        break
print(listan)'''



