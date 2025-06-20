# ==========================================
# Voorbeeld Opdracht
# Gegeven zijn de variabelen a = 3 en b = 10. Evalueer met een if statement of a groter is dan b. Als dat zo is, print dan a. Als dat niet zo is, print dan b.
# ==========================================

a = 3
b = 10

if a > b:
    print(a)
else:
    print(b)

# ==========================================
# Opgave 1:
# Gegeven is een int input getal_1 en getal_2 en drie print methodes. Schrijf een if statement dat controleert of getal1 een veelvoud is van getal2, andersom of dat beide getallen geen veelvoud zijn van de ander.
# Zet de juiste print methode op de goede plek in je if statement.
# Voorbeeld goede output: 10 is een veelvoud van 5
# ==========================================


getal_1 = int(input("voer een getal in: "))
getal_2 = int(input("voer een getal in: "))

if getal_1 > getal_2:
    print(f'{getal_1} is een veelvout van {getal_2}')
else:
    print(f'{getal_2} is een veelvout van {getal_1}')



# ==========================================
# Opgave 2:
# De basisprijs van een bioscoopkaartje is 12 euro.

# - Kinderen tot 5 jaar zijn gratis
# - kinderen van 5 tot 12 jaar betalen de halve prijs.
# - Personen tussen 13 en 54 jaar moeten de volle prijs betalen
# - vanaf 55 jaar is de toegang weer gratis.

# Maak een programma dat de te betalen prijs afdrukt nadat je de leeftijd hebt ingevoerd als input.
# Voorbeeld output: Voor de leeftijd 10 jaar is de prijs: 6.0
# ==========================================

leeftijd = int(input("voer je leeftijd in: "))

if leeftijd < 5:
    print(f'Je kaartje kost niks, je mag gratis naar binnen omdat je onder de 5 jaar bent.')
elif leeftijd < 12:
    print(f'Je bent tussen de 5 en 12 jaar, het kaartje kost 6 euro.')
elif leeftijd < 54:
    print(f'U bent tussen de 13 en 54 jaar, het kaartje kost 12 euro.')
else:
    print(f'U bent ouder dan 55, het kaartje kost niks. U mag gratis van de film genieten.')

# ==========================================
# Opgave 3:
# Schrijf een programma dat 3 gehele getallen (integers) sorteert. De willekeurige inputs worden opgeslagen in de
# variabelen num1, num2 en num3 (maak deze variabelen met inputs zelf aan). Schrijf een if statement die het laagste getal in num1 stopt,
# het middelste getal in num2 en het hoogste getal in num3.

# Print de variabelen in de volgorde num1, num2, num3.
# Voorbeeld input: 3 1 2
# Voorbeeld output: 1 2 3
# ==========================================

number1 = int(input('voer een getal in: '))
number2 = int(input("voer een getal in: "))
number3 = int(input("voer een getal in: "))

if number1 > number2:
    number1, number2 = number2, number1
if number2 > number3:
    number2, number3 = number3, number2
if number1 > number2:
    number1, number2 = number2, number1
print(number1, number2, number3)




# ==========================================
# Opgave 4:
# Gegeven is de variabele 'totaal' met een waarde van 0. Schrijf een programma dat herhaaldelijk een getal als input vraagt.
# Elk getal dat je invoert moet moet worden opgeteld bij het totaal. Als je 0 invoert moet het programma stoppen en met een print
# statement het totaal en het gemiddelde van de getallen afdrukken (dus totaal / aantal inputs). Als er geen getallen zijn ingevoerd
# moet de volgende string worden geprint: "er zijn geen getallen ingevoerd".
#
# Voorbeeld input: 2, 4, 6, 0
# Voorbeeld output: totaal: 12, gemiddelde: 4.0
# ==========================================

total = 0
printed_numbers = 0

input_amount = int(input('Enter a number: '))

while input_amount != 0:
    total += input_amount
    printed_numbers += 1
    input_amount = int(input('Enter a number: '))

if  printed_numbers != 0:
    print(f"total: {total}")
    print(f"average: {total / printed_numbers}")

else:
    print('No numbers were entered.')




# ==========================================
# Opgave 5:
# Schrijf een input die een integer verwacht en stop deze in de variabele “factor”.
# Schrijf daarna een programma dat de tafel van “factor” afdrukt, Print de tafel van 'factor' van 1 tot en met 10.

# Voorbeeld input: 5
# Voorbeeld output:
#   1 x 5 = 5
#   2 x 5 = 10
#   3 x 5 = 15 # enz. tot en met 10
# ==========================================


factor = int(input('Enter a number: '))

for teller in range(1, 11):
    result = teller * factor
    print(f'{teller} x {factor} = {result}')

