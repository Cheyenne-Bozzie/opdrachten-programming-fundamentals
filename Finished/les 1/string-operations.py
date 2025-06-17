# ==========================================
# Voorbeeld Opdracht
# Gegeven is de string ‘Python’ en het getal 3.
# Maak met deze variabelen de volgende string: ‘Python Python Python’ Gebruik een operator.
# ==========================================

woord = 'Python '
aantal_keer = 3

print(woord * aantal_keer)  # Het resultaat is: Python Python Python

print('Python ' * 3)

# ==========================================
# Opgave 1:
# Maak de volgende zin in Python: Bello is 4 jaar. Dit is 28 jaar in mensenjaren.
# Je hebt de volgende variabelen: leeftijd_hond = 4 en naar_mensen_jaren = 7
# Maak een variabele aan genaamd 'mensen_jaren’. Ken daar de waarde aan toe van leeftijd_hond maal naar_mensen_jaren.
# Schrijf nu de zin met de print() methode.

# Verwachte uitkomst: Bello is 4 jaar. Dit is 28 jaar in mensenjaren.
# ==========================================

leeftijd_hond = 4
naar_mensen_jaren = 7
print('Bello is', leeftijd_hond, 'jaar. Dit is ', leeftijd_hond * naar_mensen_jaren, 'in mensenjaren.')

# ==========================================
# Opgave 2:
# Wat zijn de datatypes van de gegeven variabelen?
# Bedenk het antwoord vooraf en check het met de print() methode die het type van de variabele print.
# ==========================================

variabele_een = '5'
variabele_twee = 1 / 1
variabele_drie = 'Python' * 3

print(variabele_een)

# ==========================================
# Opgave 3:
# Niet alle variabele namen zijn toegestaan in Python. Sommige namen zijn gereserveerd voor Python zelf (keywords).
# Welke van de volgende variabele namen kun je gebruiken zonder dat je een foutmelding krijgt? Bedenk het antwoord vooraf en check het door de variabelen aan te maken.

# a.     and = ‘something’
# b.     while = ‘something’
# c.     break = ‘something’
# d.     none = ‘something’
# ==========================================

# A,B en C kunnen niet gebruikt worden.

# ==========================================
# Opgave 4:
# Schrijf een goede variabele naam voor:

# A. Het totale aantal van een product (bananen)
# B. De minimale toegestane lengte voor een attractie in een pretpark
# C. Het grootste getal in een rij met getallen

# Denk ook aan de schrijfconventies voor variabele namen.
# ==========================================
# A. totaal_aantal_bananen
# B. min_lengte_voor_attractie
# C. max_getal


# ==========================================
# Opgave 5:
# Maak onderstaande opgaven
# Maak van het getal 3.14 een 3. Je mag alleen de typecast functie gebruiken
# ==========================================

print(int(3.14))

# ==========================================
# Opgave 6:
# Gegeven zijn mijn_variabele = 5 en print(mijn_variabele * 3)
# Zorg ervoor dat de uitkomst van de print() methode ‘555’ is zonder dat je een andere getalswaarde toekent aan mijn_variabele.
# De gegeven code mag je niet aanpassen, maar je mag wel extra code toevoegen.
#
# Verwachte uitkomst: 555
# ==========================================

mijn_variabele = 5
print(str(mijn_variabele) * 3)  # Het resultaat is: 555

