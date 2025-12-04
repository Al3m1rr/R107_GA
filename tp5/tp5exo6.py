t = input("Entrez une phrase : ")

n = 0
for _ in t:
    n += 1
print("1) La taille de la chaîne est de :", n)


v = 0
voy = "aeiouyAEIOUY"
for c in t:
    if c in voy:
        v += 1

if n > 0:
    pourcentage = v * 100 / n
else:
    pourcentage = 0

print("2) Le pourcentage de voyelles contenues dans la phrase est de :", pourcentage)


mot = "wagon"
i = -1
for k in range(n - len(mot) + 1):
    ok = True
    for j in range(len(mot)):
        if t[k + j].lower() != mot[j]:
            ok = False
            break
    if ok:
        i = k
        break

print("3) La première occurrence du mot 'wagon' commence à l’indice :", i)


cpt = 0
for k in range(n - len(mot) + 1):
    ok = True
    for j in range(len(mot)):
        if t[k + j].lower() != mot[j]:
            ok = False
            break
    if ok:
        cpt += 1

print("4) Le nombre total d'occurrences du mot 'wagon' est :", cpt)




