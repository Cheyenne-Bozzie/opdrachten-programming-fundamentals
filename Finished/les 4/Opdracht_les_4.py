boodschappenlijst = 'Appels', 'Melk', 'Peren', 'Kaas', 'Speklappen', 'Brood', 'Eieren', 'Bloem', 'Pizza','Cola'
# print(boodschappenlijst[1-1], boodschappenlijst[3-1])

# print(boodschappenlijst[1:4])

puzzel = ['Albatros', 'Poncho', 'vlinder', 'glitter',]

coordinaten = [(0,0),(2,0),(0,-2),(1,3),(0,3),(2,4),(1,-1)]

antwoord = []

for woord, letter in coordinaten:
    antwoord.append(puzzel[woord][letter])

print(''.join(antwoord))
