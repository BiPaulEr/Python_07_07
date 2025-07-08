def compteur(limit):
    while limit > 0:
        yield limit 
        limit = limit - 1
    print("end")

compt = compteur(5)

for i in compteur(5):
    print(i)