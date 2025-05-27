# Je werkt in een pizzaria, en je moet een programma schrijven dat de kosten van een pizza berekent.
# Er zijn 3 maten pizza's Small (s), Medium (m) en Large (l).
# Een kleine pizza kost $15, een medium pizza kost $20 en een grote pizza kost $25.
# Als de klant extra pepperoni wil, kost dit $2 voor een kleine pizza en $3 voor een medium of grote pizza.
# Als de klant extra kaas wilt, dan kost dit $1.

pizza_S = 15
pizza_M = 20
pizza_L = 25
pepperoni_S = 2
pepperoni_M_L = 3
extra_cheese = 1

pizza_choice = input('What size pizza do you want?\n')
if pizza_choice == 'Small' or pizza_choice == 'small' or pizza_choice == 's' or pizza_choice == 'S':
    print(f'You have chosen a small pizza the pizza is {pizza_S} euro\'s')

    pizza_small = input(f'Do you want pepperoni? This costs {pepperoni_S} euro\'s.\n')
    if pizza_small == 'Yes' or pizza_small == 'yes':
        pizza_S_cheese = input(f'You have chosen to add pepperoni.\nDo you also want to add extra cheese? This will cost {extra_cheese} euro.\n')
        if pizza_S_cheese == 'Yes' or pizza_S_cheese == 'yes':
            print(f'You have chosen to add pepperoni on your small pizza. You also wanted extra cheese.\nYour total will be {pepperoni_S + pizza_S + extra_cheese} euro.')

        if pizza_S_cheese == 'No' or pizza_S_cheese == 'no':
            print(f'You have chosen to add pepperoni on your small pizza. You did not want extra cheese.\nYour total will be {pepperoni_S + pizza_S} euro.')
        else: print('Invalid choice, try again.')

    elif pizza_small == 'No' or pizza_small == 'no':
        pizza_S_no_pepperoni = input(f'You have chosen not to add pepperoni.\nDo you want extra cheese? This will cost {extra_cheese} euro.\n')
        if pizza_S_no_pepperoni == 'No' or pizza_S_no_pepperoni == 'no':
            print(f'You have chosen not to add pepperoni on your small pizza. You did not want extra cheese.\nYour total will be {pizza_S} euro.')

        if pizza_S_no_pepperoni == 'Yes' or pizza_S_no_pepperoni == 'yes':
            print(f'You have chosen not to add pepperoni on your small pizza. You did want extra cheese.\nYour total will be {pizza_S + extra_cheese} euro.')
        else: print('Invalid choice, try again.')

    else: print('Invalid choice, try again.')

elif pizza_choice == 'Medium' or pizza_choice == 'medium' or pizza_choice == 'm' or pizza_choice == 'M':
    print(f'You have chosen a medium pizza the pizza is {pizza_M} euro\'s')

    pizza_medium = input(f'Do you want pepperoni? This costs {pepperoni_M_L} euro\'s.\n')
    if pizza_medium == 'Yes' or pizza_medium == 'yes':
        pizza_M_cheese = input(f'You have chosen to add pepperoni.\nDo you also want to add extra cheese? This will cost {extra_cheese} euro.\n')
        if pizza_M_cheese == 'Yes' or pizza_M_cheese == 'yes':
            print(f'You have chosen to add pepperoni on your medium pizza. You also wanted extra cheese.\nYour total will be {pepperoni_M_L + pizza_M + extra_cheese} euro.')

        if pizza_M_cheese == 'No' or pizza_M_cheese == 'no':
            print(f'You have chosen to add pepperoni on your medium pizza. You did not want extra cheese.\nYour total will be {pepperoni_M_L + pizza_M} euro.')
        else: print('Invalid choice, try again.')

    elif pizza_medium == 'No' or pizza_medium == 'no':
        pizza_M_no_pepperoni = input(f'You have chosen not to add pepperoni.\nDo you want extra cheese? This will cost {extra_cheese} euro.\n')
        if pizza_M_no_pepperoni == 'No' or pizza_M_no_pepperoni == 'no':
            print(f'You have chosen not to add pepperoni on your medium pizza. You did not want extra cheese.\nYour total will be {pizza_M} euro.')

        if pizza_M_no_pepperoni == 'Yes' or pizza_M_no_pepperoni == 'yes':
            print(f'You have chosen not to add pepperoni on your medium pizza. You did want extra cheese.\nYour total will be {pizza_M + extra_cheese} euro.')
        else: print('Invalid choice, try again.')

    else: print('Invalid choice, try again.')

elif pizza_choice == 'Large' or pizza_choice == 'large' or pizza_choice == 'l' or pizza_choice == 'L':
    print(f'You have chosen a large pizza the pizza is {pizza_L} euro\'s')

    pizza_large = input(f'Do you want pepperoni? This costs {pepperoni_M_L} euro\'s.\n')
    if pizza_large == 'Yes' or pizza_large == 'yes':
        pizza_L_cheese = input(f'You have chosen to add pepperoni.\nDo you also want to add extra cheese? This will cost {extra_cheese} euro.\n')
        if pizza_L_cheese == 'Yes' or pizza_L_cheese == 'yes':
            print(f'You have chosen to add pepperoni on your large pizza. You also wanted extra cheese.\nYour total will be {pepperoni_M_L + pizza_L + extra_cheese} euro.')

        if pizza_L_cheese == 'No' or pizza_L_cheese == 'no':
            print(f'You have chosen to add pepperoni on your large pizza. You did not want extra cheese.\nYour total will be {pepperoni_M_L + pizza_L} euro.')
        else: print('Invalid choice, try again.')

    elif pizza_large == 'No' or pizza_large == 'no':
        pizza_L_no_pepperoni = input(f'You have chosen not to add pepperoni.\nDo you want extra cheese? This will cost {extra_cheese} euro.\n')
        if pizza_L_no_pepperoni == 'No' or pizza_L_no_pepperoni == 'no':
            print(f'You have chosen not to add pepperoni on your large pizza. You did not want extra cheese.\nYour total will be {pizza_L} euro.')

        if pizza_L_no_pepperoni == 'Yes' or pizza_L_no_pepperoni == 'yes':
            print(f'You have chosen not to add pepperoni on your large pizza. You did want extra cheese.\nYour total will be {pizza_L+ extra_cheese} euro.')
        else: print('Invalid choice, try again.')