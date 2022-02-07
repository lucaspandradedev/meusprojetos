n = str(input('Digite um número: '))
nlist = []

for c in n:
    nlist.append(c)

for v in nlist:
    if v == 3:
        nlist.append('-')


print(nlist)
