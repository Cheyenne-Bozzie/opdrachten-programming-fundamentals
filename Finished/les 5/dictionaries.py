# ==========================================
# Voorbeeld Opdracht
#
# Maak een dictionary genaamd 'fruit' met daarin de sleutels 'appel' en 'banaan'.
# Geef 'appel' de value 'rood' en 'banaan' de value 'geel'.
# Print vervolgens de kleur van de banaan door de naam 'banaan' te gebruiken.
#
# Verwachte uitkomst:  geel
# ==========================================

# dictionary met kleuren als values
fruit = {'appel': 'rood', 'banaan': 'geel'}

# print de kleur van de banaan
print(fruit['banaan'])  # Het resultaat is: geel


# ==========================================
# Opdracht 1:
# Gegeven is de dictionary 'boodschappen' met daarin de keys 'Appels' en 'Brood'.
# Maak de volgende deelopdrachten. Print de uitkomst van elke opdracht om te zien of je het juiste resultaat krijgt.
#
# Opdracht 1a:
# Roep de waarde aan die hoort bij de naam 'Brood'
# Verwachte uitkomst: 2
#
# Opdracht 1b:
# Gebruik de get() methode op de waarde 'Appels' en 'Bananen'. Zorg dat als de naam niet bestaat, de tekst 'Niet gevonden' wordt geprint.
# ==========================================

# 1a
boodschappen = {'Appels': 6, 'Brood': 2}
print(boodschappen['Brood'])

# 1b
lijst_Appels = boodschappen.get('Appels', 'Niet gevonden')
print(lijst_Appels)

lijst_Bananen = boodschappen.get('Bananen', 'Niet gevonden')
print(lijst_Bananen)


# ==========================================
# Opdracht 2:
# Gegeven zijn vier boodschappenlijstjes als dictionary. Je kan een if statement gebruiken en de == operator om te vergelijken.
#
# Opdracht 2a:
# Vergelijk de boodschappenlijstjes van Marie en Raj. Als de lijstjes gelijk zijn, print 'De boodschappenlijstjes zijn gelijk.'.
#
# Opdracht 2b:
# Vergelijk de boodschappenlijstjes (Marie, Raj en Jan). Als de lijstjes gelijk zijn, print 'De boodschappenlijstjes zijn gelijk.'.
# Waarom worden deze lijstjes wel/niet als gelijk beschouwd?
#
# Opdracht 2c:
# Vergelijk nu op dezelfde manier alle lijstjes. Zijn ze gelijk? Waarom wel/niet?
# ==========================================

#2a
boodschappenlijst_marie = {'Brood': 1, 'Appels': 6}
boodschappenlijst_raj = {'Brood': 1, 'Appels': 6}

if boodschappenlijst_marie == boodschappenlijst_raj:
    print('De boodschappenlijstjes zijn gelijk.')
else: print('De lijstjes zijn niet gelijk.')

# 2b
boodschappenlijst_marie = {'Brood': 1, 'Appels': 6}
boodschappenlijst_raj = {'Brood': 1, 'Appels': 6}
boodschappenlijst_jan = {'Appels': 6, 'Brood': 1}

if boodschappenlijst_marie == boodschappenlijst_raj == boodschappenlijst_jan:
    print('De boodschappenlijstjes zijn gelijk.')
else: print('De lijstjes zijn niet gelijk.')
    # Ze zijn gelijk omdat ze allemaal hetzelfde bevatten ook al staan ze in een andere volgorde.

# 2c
boodschappenlijst_marie = {'Brood': 1, 'Appels': 6}
boodschappenlijst_raj = {'Brood': 1, 'Appels': 6}
boodschappenlijst_jan = {'Appels': 6, 'Brood': 1}
boodschappenlijst_karel = {'Appels': 6, 'Brood': 25}

if boodschappenlijst_marie == boodschappenlijst_raj == boodschappenlijst_jan == boodschappenlijst_karel:
    print('De boodschappenlijstjes zijn gelijk.')
else: print('De lijstjes zijn niet gelijk.')
# Deze zijn niet gelijk omdat de waarde Brood in het lijstje van Karel 25 is ipv 1.

# ==========================================
# Opdracht 3:
# De voorraad van meubelwinkel 'Op Eigen Houtje' is als volgt:
# Gegeven is de dictionary 'meubels' met daarin de keys 'banken' en 'stoelen'.
# Maak de volgende deelopdrachten. Print de uitkomst van elke opdracht om te zien of je het juiste resultaat krijgt.
#
# Opdracht 3a:
# Er worden 6 banken verkocht. Pas de waarde van de naam 'banken' aan en print de aangepaste dictionary
# Verwachte uitkomst: {'banken': 4, 'stoelen': 20}

# Opdracht 3b:
# Er komen klachten dat klanten door eerder gekochte stoelen zijn gezakt. De winkel besluit om de stoelen uit het assortiment te halen.
# Verwijder de naam 'stoelen' (en daarmee ook de bijbehorende value) uit de dictionary en print de aangepaste dictionary.
# Verwachte uitkomst: {'banken': 4}

# Opdracht 3c:
# De winkel gaat tafels verkopen en koopt er gelijk 15 in. Voeg de naam 'tafels' toe met een waarde van 15 en print de aangepaste dictionary.
# Verwachte uitkomst: {'banken': 4, 'tafels': 15}
# ==========================================

meubels = {'banken': 10, 'stoelen': 20}

# 3a
meubels['banken'] -= 6
print(meubels)

# 3b
del meubels['stoelen']
print(meubels)

# 3c
meubels['tafels'] = 15
print(meubels)

# ==========================================
# Opdracht 4:
# Docent Erik heeft proefwerken van studenten nagekeken en de cijfers in een dictionary opgeslagen.
# Erik komt erachter dat hij een fout heeft gemaakt en moet de cijfers met een factor 1,5 vermenigvuldigen.
# Met als enige uitzondering dat een cijfer nooit hoger mag zijn dan een 10.
# Print de uitkomst om te zien of je het juiste resultaat krijgt.

# Gegeven is de dictionary 'cijfers' met daarin de keys 'Jaap', 'Winnie', 'Jeroen' en 'Lana' en hun cijfers.
# Verwachte uitkomst: {'Jaap': 4.5, 'Winnie': 6.0, 'Jeroen': 10, 'Lana': 10}
# ==========================================

cijfers = {'Jaap': 3, 'Winnie': 4, 'Jeroen': 9, 'Lana': 10}

for naam in cijfers:
    huidig_cijfer = cijfers[naam]
    nieuw_cijfer = huidig_cijfer * 1.5

    if nieuw_cijfer > 10:
        nieuw_cijfer = 10
    cijfers[naam] = nieuw_cijfer

print(cijfers)



# ==========================================
# Opdracht 5:
# De eigenaar van dierentuin 'Het Zootje' heeft een lijst met dieren en hun aantallen. De dieren en hun aantallen zijn opgeslagen in een dictionary.
# Maak onderstaande deelopdrachten.
#
# Opdracht 5a:
# De eigenaar wil de dieren op alfabetische volgorde zien. Sorteer de dieren op naam en print de dictionary uit.
# Verwachte uitkomst: {'Aap': 5, 'Giraffe': 2, 'Leeuw': 3, 'Olifant': 4, 'Zebra': 1}
#
# Opdracht 5b:
# Nu wil de eigenaar in een oogopslag wat het hoogste aantal is en het laagste. Sorteer nu de aantallen van hoog naar laag en print de dictionary uit. (De keys hoef je niet te printen)
# ==========================================

# 5a
dieren = {'Olifant': 5, 'Zebra': 8, 'Aap': 12, 'Giraffe': 3, 'Neushoorn': 7}

alfabetische_dieren = sorted(dieren)
print(alfabetische_dieren)

# 5b
dieren = {'Olifant': 5, 'Zebra': 8, 'Aap': 12, 'Giraffe': 3, 'Neushoorn': 7}
gesorteerde_aantal_dieren = sorted(dieren.items(), key=lambda item: item[1], reverse=True)

lijst_dieren = []
for naam, aantal in gesorteerde_aantal_dieren:
    lijst_dieren.append(str(aantal))
print(", ".join(lijst_dieren)+'.')
