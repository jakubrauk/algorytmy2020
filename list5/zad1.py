import random
a = int(input("rozmair grafu: "))
slownik = {}
for i in range(a):
    slownik.update({i: [random.randint(1,a-1)]})
print(slownik)
for i in range(a):
    for nati in slownik[i]:
        if i not in slownik[nati]:
            slownik[nati].append(i)
print(slownik)

c = [0]*a
cn = 0
stos = []
for i in range(a):
    if c[i]>0:
        continue
    cn += 1
    stos.append(i)
    c[i] = cn
    while len(stos) > 0:
        v = stos.pop()
        for u in slownik[v]:
            if c[u] > 0:
                continue
            stos.append(u)
            c[u]=cn

print("Liczba składowych: ", cn)
for i in range(1, cn+1):
    print("Składowa numer: ", i)
    for j in range(a):
        if c[j] == i:
            print("Wierzchołek: ", j)
