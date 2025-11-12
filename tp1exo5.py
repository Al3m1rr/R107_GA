jour = int(input("Saisissez une valeur pour le jour : "))
heure = int(input("Saisissez une valeur l'heure : "))
minutes = int(input("Saisissez une valeur les minutes : "))
minutes_total = (jour*24*60) + (heure*60) + minutes
print("Depuis le début du mois il y a",minutes_total,"minutes d'écoulés")
