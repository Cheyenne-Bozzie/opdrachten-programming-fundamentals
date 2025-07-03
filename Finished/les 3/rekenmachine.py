# Schrijf een simpele rekenmachine. De gebruiker moet twee getallen en een operatie invoeren.
# Het programma moet de berekening uitvoeren en het resultaat printen.

# Voorbeeld:
# Enter the first number: 5.1
# Enter the second number: 3
# Enter the operation: +
# The result is: 8.1

# Het programma moet de volgende operaties ondersteunen: +, -, *, /
# Als de gebruiker een ongeldige operatie invoert, moet het programma "Invalid operation" printen.

number_1 = float(input("Enter a number: "))
operator = input("Enter an operator +, -, *, or /: ")
number_2 = float(input("Enter a number: "))

if operator == '+':
    print(f'{number_1} + {number_2} = {number_1 + number_2}')
elif operator == '-':
    print(f'{number_1} - {number_2} = {number_1 - number_2}')
elif operator == '*':
    print(f'{number_1} * {number_2} = {number_1 * number_2}')
elif operator == '/':
    print(f'{number_1} / {number_2} = {number_1 / number_2}')
else: print('Invalid operator chosen.')