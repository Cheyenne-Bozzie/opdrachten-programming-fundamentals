# Schrijf een programma dat een gebruiker om een wachtwoord vraagt. De gebruiker heeft maximaal 3 pogingen om het juiste wachtwoord in te voeren. Als het juiste wachtwoord is ingevoerd, print je een succesbericht en beëindig je de loop. Als de gebruiker 3 pogingen fout invoert, geef je een bericht dat de toegang is geweigerd.
#
# Stappenplan:
#
# 1. Stel een vast wachtwoord in (bijvoorbeeld: "python123"), door daar een variabele voor te maken.
# 2. Vraag de gebruiker om het wachtwoord in te voeren.
# 3. Gebruik een while-loop om de gebruiker maximaal 3 kansen te geven om het juiste wachtwoord in te voeren.
# 4. Als de gebruiker het juiste wachtwoord invoert, beëindig dan de loop met een succesbericht.
# 5. Als de gebruiker na 3 pogingen nog steeds het verkeerde wachtwoord invoert, geef een foutmelding.

correct_password = 'python123'
max_tries = 3
tries_teller = 0

while tries_teller < max_tries:
    input_password = input(f'Enter a password (Tries left: {tries_teller}/{max_tries}):\n')

    if input_password== correct_password:
        print("Succes!")
        break
    else:
        print("Wachtwoord incorrect. Probeer opnieuw.)")
        tries_teller += 1

if tries_teller == max_tries:
    print('You entered the wrong password too many times, entry blocked.')