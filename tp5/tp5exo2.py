notes = []
coeffs = []
for i in range(5):
    s = input(f"Note et coefficient du module {i+1} (ex : 12.5 3) : ").split()
    notes.append(float(s[0]))
    coeffs.append(int(s[1]))

m = 0
t = 0
for i in range(5):
    m += notes[i] * coeffs[i]
    t += coeffs[i]
m /= t

adm = True
for n in notes:
    if n < 8:
        adm = False
if m <= 10:
    adm = False

print(m)
if adm:
    print("admis")
else:
    print("non admis")

