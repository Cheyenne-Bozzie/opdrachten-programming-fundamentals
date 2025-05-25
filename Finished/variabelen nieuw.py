# ==========================================
# Voorbeeld Opdracht
# Gegeven is een variabele 'leeftijd' met de waarde 25. Print de zin 'Mijn leeftijd is 25'
# ==========================================

leeftijd = 25
print('Mijn leeftijd is', leeftijd)  # Het resultaat is: Mijn leeftijd is 25

# ==========================================
# Opgave 1.
# Gegeven is een variabele 'naam' met de waarde 'Jan' en de variabele 'leeftijd' met de waarde 25. Print de zin 'Mijn naam is Jan en ik ben 25 jaar oud'. Verander daarna de leeftijd naar 30 en print de zin opnieuw.
#
# Verwachte uitkomst is: 'Mijn naam is Jan en ik ben 25 jaar oud' en 'Mijn naam is Jan en ik ben 30 jaar oud'
# ==========================================

naam = 'Jan'
leeftijd = 25

print('Mijn naam is', naam, 'en ik ben', leeftijd, 'jaar oud.')

# ==========================================
# Opgave 2.
# Gegeven zijn een aantal variabelen. Wat zijn de datatypes van de variabelen als je ze print met de type() method? Bedenk vooraf wat het datatype is en controleer daarna met de print functie of je het goed hebt.
# ==========================================

a = 5 / 5
print(type(a), a) = 'float'> 1.0

b = '12'
print(type(b), b) = 'str'> 12

c = 5 * 5
print(type(c), c) = int'> 25

d = 'Python' * 4
print(type(d), d) = 'str'> PythonPythonPythonPython


# ==========================================
# Opgave 3.
# Variabele namen mag je zelf verzinnen, maar niet alle namen zijn toegestaan omdat ze al gebruikt worden door Python (keywords). Welke van de volgende variabele namen zijn toegestaan en welke niet?
# ==========================================


# And = 'something' wel
# while = 'something' niet
# Break = 'something' Wel
# awaiting = 'something' Wel



# ==========================================
# Opgave 4.
# Schrijf een goede variabele naam voor onderstaande onderdelen. Denk aan de conventies voor Python variabelen.
#
# a.     Het totale aantal van het product bananen in een winkelmand
#
# b.     De minimale toegestane lengte voor een attractie in een pretpark
#
# c.     Het grootste getal in een rij met getallen
# ==========================================

# a. totaal_aantal_bananen
# b. minimale_lengte_voor_attractie
# c. grootste_getal_uit_rij



# ==========================================
# Opgave 5.
# Gegeven is de variabele 'teller' met de waarde 10. Verhoog de waarde van de teller met 1. Gebruik de samengevoegde toekenning operator. Print de waarde van de teller. Herhaal dit proces maar verlaag de teller met 2. Print opnieuw de waarde van de teller.
#
# Verwachte uitkomst is: 11 en 9
# ==========================================

teller = 10
teller += 1
print(teller) = 11

teller = 11
teller -= 2
print(teller) = 9

# ==========================================
# Opgave 6.
# Gegeven zijn de onderstaande statements. Welke van de print statements zullen een foutmelding geven en waarom?
#
# a. print(int(‘1490.99’) < Niet. ' deze tekens zijn onnodig.
#
# b. print(float(12)) < Wel. Er komt 12.0 uit
#
# c. print(int('1plus1')) < Niet. Er kan geen text in een integer staan.
#
# d. print(str(25E10)) < Wel.
# ==========================================




# ==========================================
# Opgave 7.
# Gegeven is de variabele getal_1 met waarde 3 en getal_2 met waarde 5. Schrijf de zin 'Het product van 3 en 5 is 15' door de variabelen te gebruiken in de zin. Pas een f-string toe.
# ==========================================

getal_1 = 3
getal_2 = 5

print(f'Het product van  {getal_2} x {getal_1} is 15')