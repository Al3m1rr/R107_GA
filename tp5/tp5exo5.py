h = float(input("Nombre d'heures travaillées : "))
s = float(input("Salaire horaire : "))
if h <= 160:
    sal = h * s
elif h <= 200:
    sal = 160 * s + (h - 160) * s * 1.25
else:
    sal = 160 * s + 40 * s * 1.25 + (h - 200) * s * 1.5
print(sal)
