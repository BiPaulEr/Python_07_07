lsite_etudiants  = [{"Name" : "Martin", "Notes": [3, 4, 5, 6] }, 
{"Name" : "Paul", "Notes": [14, 14, 15, 16] }, 
{"Name" : "Ernest", "Notes": [0, 5, 10, 20] }]

print(list(map(lambda eleves : eleves["Notes"], lsite_etudiants)))