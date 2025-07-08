liste = ["A", "B", "C", "D"]

liste2 = [caracter.lower() for caracter in liste if caracter != "B"]
gen2 = (caracter.lower() for caracter in liste if caracter != "B")
liste.append("QUOI")
print(liste2)

print(gen2)
for i in gen2:
    print(i)
