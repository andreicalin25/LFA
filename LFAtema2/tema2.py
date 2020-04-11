def cauta_bucle(l1, l2, elem):
    for i in range(len(l1)):
        if elem == l1[i] == l2[i]:
            return i
    return False


def elimina_nod(s, r, e, nod):
    s1 = []
    r1 = []
    e1 = []

    for i in range(len(e)):
        if e[i] == nod:

            for j in range(len(s)):
                if s[j] == nod:
                    s1.append(s[i])
                    e1.append(e[j])

                    if r[i] == "lambda" and r[j] == "lambda":
                        r1.append("lambda")
                    elif r[i] == "lambda":
                        r1.append(r[j])
                    elif r[j] == "lambda":
                        r1.append(r[i])
                    else:
                        r1.append(r[i] + r[j])

    for i in range(len(e)):
        if e[i] != nod and s[i] != nod:
            s1.append(s[i])
            r1.append(r[i])
            e1.append(e[i])
    print('\n')
    print("elimin nodul " + nod)
    print(s1)
    print(r1)
    print(e1)
    return s1, r1, e1


def elimina_nod_bucla(s, r, e, nod, poz_bucla):
    s1 = []
    r1 = []
    e1 = []

    # daca pe bucla avem mai multe caractere, acestea trebuiesc puse in paranteza inainte de stelare
    if len(r[poz_bucla]) > 1:
        r[poz_bucla] = '(' + r[poz_bucla] + ')'

    for i in range(len(e)):
        if e[i] == nod and i != poz_bucla:

            for j in range(len(s)):
                if s[j] == nod and j != poz_bucla:
                    s1.append(s[i])
                    e1.append(e[j])

                    if r[i] == "lambda" and r[j] == "lambda":
                        r1.append(r[poz_bucla] + '*')
                    elif r[i] == "lambda":
                        r1.append(r[poz_bucla] + '*' + r[j])
                    elif r[j] == "lambda":
                        r1.append(r[i] + r[poz_bucla] + '*')
                    else:
                        r1.append(r[i] + r[poz_bucla] + '*' + r[j])

    for i in range(len(e)):
        if e[i] != nod and s[i] != nod:
            s1.append(s[i])
            r1.append(r[i])
            e1.append(e[i])
    print('\n')
    print("elimin nodul " + nod)
    print(s1)
    print(r1)
    print(e1)
    return s1, r1, e1


def verifica_duplicate(l1, l2):
    for i in range(len(l1) - 1):
        for j in range(i+1, len(l1)):
            if l1[i] == l1[j] and l2[i] == l2[j]:
                return i, j
    return False


def elimina_duplicate(s, r, e, i, j):
    s.pop(j)
    e.pop(j)
    r[i] = '(' + r[i] + '+' + r[j] + ')'
    r.pop(j)
    return s, r, e




f = open("automat2.txt")
nodI = f.readline()
nodI = nodI[:-1]
noduri = [i for i in f.readline().split()]
finale = [i for i in f.readline().split()]

S = []
R = []
E = []

for muchie in f.readlines():
    a, b, c = muchie.split()
    S.append(a)
    R.append(b)
    E.append(c)

for i in finale:
    S.append(i)
    R.append("lambda")
    E.append('F')

print(S)
print(R)
print(E)

for nod in noduri:
    poz_bucla = cauta_bucle(S, E, nod)

    if poz_bucla == False:
        S, R, E = elimina_nod(S, R, E, nod)
    else:
        S, R, E = elimina_nod_bucla(S, R, E, nod, poz_bucla)

    if verifica_duplicate(S, E):
        d1, d2 = verifica_duplicate(S, E)
        print("sunt duplicate")
        S, R, E = elimina_duplicate(S, R, E, d1, d2)
        print(S)
        print(R)
        print(E)


if nodI in E:
    reg = R[E.index(nodI)]
    reg = '(' + reg + ')*' + R[E.index('F')] if R[E.index('F')] != "lambda" else '(' + reg + ')*'
else:
    reg = R[E.index('F')]

print('\n' + reg)

