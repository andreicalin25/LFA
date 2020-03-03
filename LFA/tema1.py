f = open("citire1.txt")
noduri = f.readline()
l_adiacenta={}

for nod in noduri.split():
    l_adiacenta[nod]=[]

initial=f.readline()
initial=initial[:-1]
finale=f.readline().split()

muchii = f.readlines()

for muchie in muchii:
    I, r, F= muchie.split()
    l_adiacenta[I].append((r, F))

for v,k in l_adiacenta.items():
    print(v, ':', *k)

cuvant = input("\ncuvantul dat este: ")

if cuvant=='':
    if initial in finale:
        print("cuvantul dat este valid")
    else:
        print("cuvantul dat este invalid")
else:
    curent=initial
    ajuns_final=True

    for i in cuvant[:-1]:
        gasit=False

        for muchie in l_adiacenta[curent]:
            if i==muchie[0]:
                curent=muchie[1]
                gasit=True
                break

        if gasit==False:
            print("cuvantul dat este invalid")
            ajuns_final=False

    if ajuns_final==True:
        i=cuvant[-1]
        gasit_muchie=False
        for muchie in l_adiacenta[curent]:
            if i==muchie[0]:
                if muchie[1] in finale:
                    print("cuvantul dat este valid")
                else:
                    print("cuvantul dat este invalid")
                gasit_muchie=True

        if gasit_muchie==False:
            print("cuvantul dat este invalid")
