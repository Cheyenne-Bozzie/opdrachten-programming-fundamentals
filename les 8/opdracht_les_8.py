import os

TODO_FILE = 'TODO.txt'

def main():
    while True:
        print("\nTODO Applicatie")
        print("1. Bekijk TODO-lijst")
        print("2. Voeg TODO-item toe")
        print("3. Verwijder TODO-item")
        print("4. Stop")
        choice = input("Maak uw keuze (1-4): ").strip()

        if choice == '1':
            see()

def see():
    with open('les 8/TODO.txt', 'r') as file:
        print(file.read())

    def add():
        with open('TODO.txt', 'w', newline='') as TODOS:
            txtwrite = TODOS.write(input('Voeg iets toe: '))
main()