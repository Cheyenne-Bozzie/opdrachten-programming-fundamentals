# Boeken geleend door Groep 1

groep1 = {"Harry Potter", "De Hobbit", "De Da Vinci Code", "De Hobbit", "De Da Vinci Code", "Twilight", "De Vijfde Golf", "Harry Potter", "De Hobbit"}

#Boeken geleend door Groep 2

groep2 = {"De Da Vinci Code", "De Alchemist", "Harry Potter", "De Hobbit", "Twilight", "The Hunger Games", "Gone Girl", "Twilight", "De Hobbit"}

print(f'De boeken geleend door groep 1 zijn: {groep1}')
print(f'De boeken geleend door groep 2 zijn: {groep2}\n')

geleend_door_beide_groepen = groep1.intersection(groep2)
print(f'De boeken die door allebei de groepen zijn geleend zijn: {geleend_door_beide_groepen}')

boeken_geleend_groep1_niet_groep2 = groep1.difference(groep2)
print(f'De boeken die alleen door groep 1 geleend zijn en niet door groep 2: {boeken_geleend_groep1_niet_groep2}')

boeken_geleend_groep2_niet_groep1 = groep2.difference(groep1)
print(f'De boeken die alleen door groep 2 geleend zijn en niet door groep 1: {boeken_geleend_groep2_niet_groep1}')