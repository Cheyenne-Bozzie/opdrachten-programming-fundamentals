
while True:
    try:
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
        else:
            print('Invalid operator chosen.\n')

    except ValueError:
        print('Invalid input.\n')
        continue

    retry = input('Do you want to try again? Yes/No: ')
    if retry.lower() != "Yes":
        print("Goodbye.")
        break
