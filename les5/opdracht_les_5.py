# Opdracht beschrijving:
# Beheer een lijst met studenten en hun cijfers
# Je gaat een programma schrijven dat een lijst met studenten en hun behaalde cijfers
# beheert. Je gebruikt hiervoor een lijst van tuples. Elke tuple bevat de naam van een
# student en zijn of haar cijfer.
# Stappen:

# 1. Maak een lijst van tuples, waarbij elke tuple bestaat uit een student en zijn/haar cijfer.
# Bijvoorbeeld:
# studenten = [("Alice", 8.5), ("Bob", 7.0), ("Charlie", 6.2),
# ("Diana", 9.1)]

studenten = [("Alice", 8.5), ("Bob", 7.0), ("Charlie", 6.2),("Diana", 9.1)]

# 2. Gebruik een for-loop om:
#  - Alle namen van de studenten met hun bijbehorende cijfer af te drukken in een nette
# opsomming.
#  - De gemiddelde score van de studenten te berekenen.

totale_score = 0.0
aantal_studenten = 0

for student in studenten:
    naam = student[0]
    cijfer = student[1]

    print(f'- {naam}: {cijfer}')

    totale_score += cijfer
    aantal_studenten += 1

# 3. Toon de volgende resultaten aan het einde van het programma:
#  - De gemiddelde score van alle studenten.
#  - De naam en het cijfer van de student met het hoogste cijfer

    hoogste_score = -1.0
    student_hoogste_score = ''

    if cijfer > hoogste_score:
        hoogste_score = cijfer
        student_hoogste_score = naam

if aantal_studenten > 0:
    gemiddelde_score = totale_score / aantal_studenten
    print(f'De gemiddelde score van de studenten is: {gemiddelde_score:.1f}')
    print(f'De student met de hoogste score is: {student_hoogste_score} met een {hoogste_score}')
else:
    print('Error.')

# BONUS (optioneel):
# - Vraag de gebruiker om studenten en cijfers toe te voegen aan de lijst via `input()`.
# - Laat de gebruiker zoeken op naam om het cijfer van een specifieke student te zien.
# - Sorteer de lijst op cijfers en druk deze af

while True