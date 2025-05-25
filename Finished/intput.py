# ==========================================
# Voorbeeld Opdracht
# Voer je naam in met de input() methode en print daarna je naam in de console.
# ==========================================

naam = input('Voer je naam in: ')  # voorbeeld invoer: Bart
print('Je naam is: ', naam)  # Het resultaat is: Je naam is: Bart

# ==========================================
# Opgave 1:
# Gegeven is het woord 'Python'. Schrijf een programma dat de gebruiker vraagt om input. Als de gebruiker het woord 'Python' invoert, print dan de boolean True, anders print False.
# ==========================================

user_input = input('Voer een woord in: ')
if user_input == 'Python':
    print('True')
else:
    print('False')

woord = 'Python'
invoer = input('Voer een woord in:')
print(invoer == woord)

# ==========================================
# Opgave 2:
# Schrijf een programma dat de gebruiker vraagt om een getal. Voer daarna nog een getal in en print de som van de twee getallen.

# Verwachte uitkomst bij invoer van getallen 2 en 3:  De som van 2 en 3 is : 5
# ==========================================

getal_een = float(input("Voer een getal in :"))
getal_twee = 3
print('de som van', getal_een, 'en', getal_twee, 'is:', getal_een + getal_twee)