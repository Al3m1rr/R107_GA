minutes = int(input("Entrez le nombre de minutes écoulées depuis le début du mois : "))


minutes_par_jour = 24 * 60


jours_ecoules = minutes // minutes_par_jour


minutes_restantes = minutes % minutes_par_jour


heures = minutes_restantes // 60
minutes_finales = minutes_restantes % 60


jour_du_mois = jours_ecoules 

print(f"La date associée à {minutes} minutes écoulées depuis le début du mois est : Jour {jour_du_mois} du mois")
print(f"Heure : {heures:02d}:{minutes_finales:02d}")
