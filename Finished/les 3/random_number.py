# In deze opdracht ga je een script schrijven waarbij de gebruikter een geheim getal moet raden.
#
# Stappenplan:
#
# 1. Maak een variable "random_getal" en geef deze een willekeurige integer waarde tussen 1 en 10.
# 2. Vraag de gebruiker om het getal te raden
# 3. Gebruik een while-loop die blijft draaien zolang de gebruiker het verkeerde getal raadt.
# 4. Geef feedback of de ingevoerde waarde te hoog of te laag is.
# 5. Wanneer de gebruiker het juiste getal raadt, beëindig de loop en print een felicitatiebericht.
#
# BONUS: Gebruik `import random` en `random.randomInt(1, 10)` om je geheime getal mee te maken
# en deze zo ook voor jezelf geheim te houden.


import random
random_getal = random.randint(1, 10)
geraden_getal = 0

while geraden_getal != random_getal:
    try:
        geraden_getal = int(input('Raad een getal tussen de 1 en 10: '))

        if not (1 <= geraden_getal <= 10):
            print("Dat is geen getal tussen 1 en 10. Probeer het opnieuw.")
            continue

        if random_getal > geraden_getal:
            print('Fout! Je zat te laag.')
        elif random_getal < geraden_getal:
            print('Fout! Je zat te hoog.')

    except ValueError:
        print('Onjuist getal.')

print(f'Succes! Het getal was {random_getal}')
