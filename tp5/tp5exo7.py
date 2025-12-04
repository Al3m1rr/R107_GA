import os
import datetime


f1 = input("Entrez le nom du premier fichier (ex: f1.txt) : ")
f2 = input("Entrez le nom du deuxième fichier (ex: f2.txt) : ")


if os.path.isfile(f1):
    taille_f1 = os.path.getsize(f1)
    print(f"La taille de '{f1}' est de {taille_f1} octets.")
else:
    print(f"Le fichier '{f1}' n'existe pas.")

if os.path.isfile(f2):
    taille_f2 = os.path.getsize(f2)
    print(f"La taille de '{f2}' est de {taille_f2} octets.")
else:
    print(f"Le fichier '{f2}' n'existe pas.")


if os.path.isfile(f1) and os.path.isfile(f2):
    t1 = os.path.getmtime(f1)
    t2 = os.path.getmtime(f2)

    if t1 > t2:
        print(f"Le fichier le plus récent est '{f1}', modifié le {datetime.datetime.fromtimestamp(t1)}.")
    else:
        print(f"Le fichier le plus récent est '{f2}', modifié le {datetime.datetime.fromtimestamp(t2)}.")


