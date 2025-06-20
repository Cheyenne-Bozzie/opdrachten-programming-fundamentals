#
# Schrijf een programma voor kassa medewerkers waarin je een bedrag (in centen) invoert, bijvoorbeeld 87 cent,
# en het programma geeft terug hoeveel munten van 50, 20, 10, 5, en 1 cent je terug zou moeten geven.
# Het programma gebruikt een while-loop om de berekening stap voor stap uit te voeren,
# telkens de grootste munt eraf halend totdat het bedrag nul is.
#
# Stappenplan:
#
# 1. Vraag de gebruiker om een bedrag in centen in te voeren (bijvoorbeeld 87).
#       (Bonus: check of de gebruiker niet meer dan 100 invoert)
# # 2. Gebruik een while-loop om telkens de grootste muntwaarde van het bedrag af te trekken.
#    De loop stopt wanneer het bedrag nul is.
# 3. Maak in de while-loop, voor elke munt waarde een (nested) if-statement, waarin je het volgende doet:
#       - Bereken hoevaak die muntwaarde in het bedrag past.
#       - Trek zo vaak de muntwaarde van het bedrag af,
#         zodat de volgende iteratie van de while-loop het aangepast bedrag gebruikt
#       - Print hoeveel munten van deze waarde de gebruiker terug moet krijgen.
#
# Bonus: Breid het programma uit, zodat het ook briefgeld en euro munten kan teruggeven.

# De beschikbare muntwaarden

vijfhonderd_euro = 500.00
honderd_euro = 100.00
vijftig_euro = 50.00
twintig_euro = 20.00
tien_euro = 10.00
vijf_euro = 5.00
twee_euro = 2.00
een_euro = 1.00
vijftig_cent = 0.50
twintig_cent = 0.20
tien_cent = 0.10
vijf_cent = 0.05
een_cent = 0.01

while True:
    try:
        bedrag = float(input('Vul een bedrag in: '))
        if bedrag < 0:
            print('Dat bedrag was te laag. Vul een hoger getal in boven de 0.')
        else:
            print(f'U heeft {bedrag} ingevoerd. Uw wisselgeld word nu berekend.')
            break
    except ValueError:
        print('Ongeldige invoer.')

print('\n U krijgt het volgende terug:')
while bedrag > 0:
        if bedrag >= vijfhonderd_euro:
            aantal_centen = bedrag // vijfhonderd_euro
            print(f'{int(aantal_centen):d} x {vijfhonderd_euro:.2f} euro')
            bedrag -= (aantal_centen * vijfhonderd_euro)

        elif bedrag >= honderd_euro:
            aantal_centen = bedrag // honderd_euro
            print(f'{int(aantal_centen):d} x {honderd_euro:.2f} euro')
            bedrag -= (aantal_centen * honderd_euro)

        elif bedrag >= vijftig_euro:
            aantal_centen = bedrag // vijftig_euro
            print(f'{int(aantal_centen):d} x {vijftig_euro:.2f} euro')
            bedrag -= (aantal_centen * vijftig_euro)

        elif bedrag >= twintig_euro:
            aantal_centen = bedrag // twintig_euro
            print(f'{int(aantal_centen):d} x {twintig_euro:.2f} euro')
            bedrag -= (aantal_centen * twintig_euro)

        elif bedrag >= tien_euro:
            aantal_centen = bedrag // tien_euro
            print(f'{int(aantal_centen):d} x {tien_euro:.2f} euro')
            bedrag -= (aantal_centen * tien_euro)

        elif bedrag >= vijf_euro:
            aantal_centen = bedrag // vijf_euro
            print(f'{int(aantal_centen):d} x {vijf_euro:.2f} euro')
            bedrag -= (aantal_centen * vijf_euro)

        elif bedrag >= twee_euro:
            aantal_centen = bedrag // twee_euro
            print(f'{int(aantal_centen):d} x {twee_euro:.2f} euro')
            bedrag -= (aantal_centen * twee_euro)

        elif bedrag >= een_euro:
            aantal_centen = bedrag // een_euro
            print(f'{int(aantal_centen):d} x {een_euro:.2f} euro')
            bedrag -= (aantal_centen * een_euro)

        elif bedrag >= vijftig_cent:
            aantal_centen = bedrag // vijftig_cent
            print(f'{int(aantal_centen):d} x {vijftig_cent:.2f} cent')
            bedrag -= (aantal_centen * vijftig_cent)

        elif bedrag >= twintig_cent:
            aantal_centen = bedrag // twintig_cent
            print(f'{int(aantal_centen):d} x {twintig_cent:.2f} cent')
            bedrag -= (aantal_centen * twintig_cent)

        elif bedrag >= tien_cent:
            aantal_centen = bedrag // tien_cent
            print(f'{int(aantal_centen):d} x {tien_cent:.2f} cent')
            bedrag -= (aantal_centen * tien_cent)

        elif bedrag >= vijf_cent:
            aantal_centen = bedrag // vijf_cent
            print(f'{int(aantal_centen):d} x {vijf_cent:.2f} cent')
            bedrag -= (aantal_centen * vijf_cent)

        elif bedrag >= een_cent:
            aantal_centen = bedrag // een_cent
            print(f'{int(aantal_centen):d} x {een_cent:.2f} cent')
            bedrag -= (aantal_centen * een_cent)

print('Al het wisselgeld is terug gegeven.')