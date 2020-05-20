def numar_terminale(x):
    nr = 0
    for i in x:
        if i in terminale:
            nr += 1
    return nr


def numar_neterminale(x):
    nr = 0
    for i in x:
        if i in neterminale:
            nr += 1
    return nr


def expand(crt, lista):
    aux.add(crt)
    # print(aux)

    for word in lista:

        k = crt
        k = k.replace('_', word)

        if numar_terminale(k) <= maxim and numar_neterminale(k) < maxim * 2 and k not in aux:

            # print(k)
            if numar_neterminale(k):
                # print(numar_neterminale(k), end="   ")

                for i in k:
                    if numar_neterminale(i):
                        k = k.replace(i, '_', 1)
                        net = i
                        break

                # print(k, d[net])

                expand(k, d[net])

            else:
                if len(k) > 1:
                    k = k.replace('λ', '')

                productii.add(k)
                # print("_________ "+k+" _____________")


f = open("data3.txt")

maxim = int(f.readline())

neterminale = [i for i in f.readline().split()]
terminale = [i for i in f.readline().split()]

d = {}

for k in f.readlines():
    a = k.split()[0]
    b = k.split()[1] if len(k.split()) > 1 else ''
    d[a] = [i for i in b.split(sep='|')]

print(d)

productii = set()
aux = set()

expand('_', d['S'])

for i in sorted(productii):
    print(i)
