n1 = input("Nom de la première personne : ")
p1 = input("Prénom de la première personne : ")
n2 = input("Nom de la deuxième personne : ")
p2 = input("Prénom de la deuxième personne : ")

p1c = p1.capitalize()
p2c = p2.capitalize()
n1u = n1.upper()
n2u = n2.upper()

l1 = p1c + " " + n1u
l2 = p2c + " " + n2u

if n1.lower() < n2.lower() or (n1.lower() == n2.lower() and p1.lower() < p2.lower()):
    print(l1)
    print(l2)
else:
    print(l2)
    print(l1)


