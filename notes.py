vijftig_cent = 50
twintig_cent = 20
tien_cent = 10
vijf_cent = 5
een_cent = 1

while True:
    try:
        bedrag_centen = int(input('Vul een bedrag in centen in (niet meer dan 100): '))
        if bedrag_centen > 100:
            print('Dat bedrag was te hoog, vul iets in onder de 100.')
        elif bedrag_centen < 0:
            print('Dat bedrag was te laag. Vul een hoger getal in boven de 0 en onder de 100.')
        else:
            print(f'U heeft {bedrag_centen} ingevoerd. Uw wisselgeld word nu berekend.')
            break
    except ValueError:
        print('Ongeldige invoer.')

print('\n U krijgt het volgende terug:')
while bedrag_centen > 0:
        if bedrag_centen >= vijftig_cent:
            aantal_centen = bedrag_centen // vijftig_cent
            print(f"{aantal_centen} x {vijftig_cent} cent")
            bedrag_centen -= (aantal_centen * vijftig_cent)

        elif bedrag_centen >= twintig_cent:
            aantal_centen = bedrag_centen // twintig_cent
            print(f"{aantal_centen} x {twintig_cent} cent")
            bedrag_centen -= (aantal_centen * twintig_cent)

        elif bedrag_centen >= tien_cent:
            aantal_centen = bedrag_centen // tien_cent
            print(f"{aantal_centen} x {tien_cent} cent")
            bedrag_centen -= (aantal_centen * tien_cent)

        elif bedrag_centen >= vijf_cent:
            aantal_centen = bedrag_centen // vijf_cent
            print(f"{aantal_centen} x {vijf_cent} cent")
            bedrag_centen -= (aantal_centen * vijf_cent)

        elif bedrag_centen >= een_cent:
            aantal_centen = bedrag_centen // een_cent
            print(f"{aantal_centen} x {een_cent} cent")
            bedrag_centen -= (aantal_centen * een_cent)


print('Al het wisselgeld is terug gegeven.')