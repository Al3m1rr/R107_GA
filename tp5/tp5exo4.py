n = int(input("Entrez une somme en euros : "))
b100 = n // 100
n %= 100
b50 = n // 50
n %= 50
b10 = n // 10
n %= 10
p2 = n // 2
p1 = n % 2
print(b100, b50, b10, p2, p1)


