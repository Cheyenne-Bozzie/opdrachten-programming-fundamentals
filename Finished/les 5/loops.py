# Tafels

# Schrijf een programma dat de tafel van een getal afdrukt.
# De gebruiker voert een getal in en het programma drukt de tafel van dat getal af.
# De tafel van 7 ziet er bijvoorbeeld als volgt uit:
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# 7 x 6 = 42
# 7 x 7 = 49
# 7 x 8 = 56
# 7 x 9 = 63
# 7 x 10 = 70


# Probeer het eerst zonder loop,
getal_input = int(input('Kies een nummer waarvan je de tafel x 1 wilt zien: '))
teller_1 = 1
tafel = getal_input * teller_1
print(f'{getal_input} x {teller_1} = {tafel}')

# Probeer het nu met een loop.
getal_input = int(input('Kies een nummer waarvan je de tafel wilt zien: '))
for teller in range(1,11):
    tafel = getal_input * teller
    print(f'{getal_input} x {teller} = {tafel}')

# --------------------------------------------------------------------------------------------

# Optellen
# Schrijf een programma dat de som van alle getallen tot een bepaalde limiet berekent.

# Bijvoorbeeld: de som van alle getallen tot 3 is 6 (1 + 2 + 3 = 6)
getal_input = int(input('Vul een getal in waarvan je een som wilt zien totdat het dat getal bereikt: '))
totale_som = 0
for teller in range(0, getal_input + 1):
    totale_som += teller
print(f"De som van alle getallen tot {getal_input} is {totale_som}.")

# --------------------------------------------------------------------------------------------

# Dit is een klassieke programmeeroefening die vaak wordt gebruikt in sollicitatiegesprekken.
# FizzBuzz

# Schrijf een programma dat de getallen van 1 tot 100 afdrukt.
# Maar voor veelvouden van drie, druk "Fizz" af in plaats van het getal.
# En voor veelvouden van vijf, druk "Buzz" af.
# Voor veelvouden van zowel drie als vijf, druk "FizzBuzz" af.

for teller in range(0, 101):

    if teller % 3 == 0 and teller % 5 == 0:
        print('Fizzbuzz')
    elif teller % 3 == 0:
        print('Fizz')
    elif teller % 5 == 0:
        print('Buzz')
    else:
        print(teller)


# --------------------------------------------------------------------------------------------


# Fibonacci-reeks

# De eerste twee getallen van de Fibonacci-reeks zijn 0 en 1.
# Elk volgend getal is de som van de twee voorgaande.
# De eerste 10 getallen van de Fibonacci-reeks zijn:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
# 0 + 1 = 1
# 1 + 1 = 2
# 1 + 2 = 3
# 2 + 3 = 5
# 3 + 5 = 8
# 5 + 8 = 13
# 8 + 13 = 21
# 13 + 21 = 34

g_input = int(input("Hoeveel Fibonacci-getallen wil je zien? "))

# De eerste twee getallen van de Fibonacci-reeks zijn 0 en 1
a = 0
b = 1

# Eerst drukken we de eerste twee getallen af

if g_input <= 0:
    print("Voer een positief getal in.")
elif g_input == 1:
    print(a)
elif g_input == 2:
    print(a, b, end= ', ')
else:
    print(a, b, end= ', ')

# Vervolgens berekenen we de volgende getallen en drukken ze af
if g_input > 2:
    for _ in range(g_input - 2):
        fib_som = a + b
        a, b = b, fib_som

        if _ == (g_input - 3):
            print(fib_som)
        else:
            print(fib_som, end=', ')
