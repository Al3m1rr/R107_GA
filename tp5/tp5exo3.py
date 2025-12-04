txt = input("Entrez un mot ou une phrase : ")
s = ""
for c in txt.lower():
    if c.isalpha():
        s += c
if s == s[::-1]:
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome.")
