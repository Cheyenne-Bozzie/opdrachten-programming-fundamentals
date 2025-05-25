### Laat python 2 getallen optellen en het resultaat printen
#  5 + 3 = 8
print(5 + 3)

### Laat python 2 getallen vermenigvuldigen en het resultaat printen
#  3 * 4 = 12
print(3 * 4)

### Geef nu het resultaat weer in een string. waar de getallen en het resultaat in staan.
print('3 x 4 = 12')

### Laat python de wortel van een getal berekenen en het resultaat printen
# De wortel van 16 is 4
# Tip gebruik ** om de wortel te berekenen

### Laat python de rest van een deling berekenen en het resultaat printen
#  De rest van 10 / 3 is 1
print(10 % 3)

### Maak een calculator die 2 getallen optelt, aftrekt, vermenigvuldigd en deelt
# Gebruik hiervoor input om de getallen te vragen
# Voer getal 1 in: 5
# Voer getal 2 in: 3
# 5 + 3 = 8
# 5 - 3 = 2
# 5 * 3 = 15
# 5 / 3 = 1.6666666666666667

getal_1_str = input('Voer een getal in: ')
getal_2_str = input('Voer een tweede getal in: ')

getal_1 = float(getal_1_str)
getal_2 = float(getal_2_str)

print('de som van', getal_1, 'plus', getal_2, 'is:', getal_1 + getal_2)
print('de som van', getal_1, 'min', getal_2, 'is:', getal_1 - getal_2)
print('de som van', getal_1, 'keer', getal_2, 'is:', getal_1 * getal_2)
print('de som van', getal_1, 'gedeeld door', getal_2, 'is:', getal_1 / getal_2)