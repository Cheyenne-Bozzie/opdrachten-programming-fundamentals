# Start test
print('Find out what hogwarts house you are.\n')
print('Choose a trait that best suits you:')
choice_1 = int(input('1: Bravery, 2: Hard Work, 3: Intelligence, 4: Ambition. Your answer: '))


if choice_1 == 1:
    print('You chose Bravery.\n')
    choice_bravery = int(input('Choose another trait: 5: Helping others, 6: Patience 8: Cunning. Your answer: '))

    if choice_bravery == 5:
        print('You chose Helping others.\n')
        choice_helping_others = int(input('Choose another trait: 9: Chivalry, 10: Fair play. Your answer: '))

        if choice_helping_others == 9:
            print('You chose Chivalry.\n')
            print("You're a Gryffindor!")
        elif choice_helping_others == 10:
            print("You chose Fair play.\n")
            print("You're a Hufflepuff!")
        else: print('Invalid choice, try again.')

    if choice_bravery == 6:
        print("You chose Patience.\n")
        choice_patience = int(input("Choose another trait: 9: Chivalry, 10: Fair play. Your answer: "))

        if choice_patience == 9:
            print("You chose Chivalry.\n")
            print("You're a Gryffindor!")
        elif choice_patience == 10:
            print("You chose Fair play\n")
            print("You're a Hufflepuff!")
        else: print("Invalid choice, try again.")

    if choice_bravery == 8:
        print("You chose Cunning.\n")
        choice_cunning = int(input("Choose another trait: 11: Wit, 12: Resourcefulness Your answer: "))

        if choice_cunning == 11:
            print("You chose Wit.\n")
            print("You're a Ravenclaw!")
        elif choice_cunning == 12:
            print("You chose Resourcefulness.\n")
            print("You're a Slytherin!")
        else:
            print('Invalid choice, try again.')


if choice_1 == 2:
      print('You chose Hard work.\n')
      choice_hard_work = int(input("Choose another trait: 5: Helping others, 6: Patience, 7: Knowledge. Your answer: "))

      if choice_hard_work == 5:
          print('You chose Helping others.\n')
          choice_helping_others = int(input('Choose another trait: 9: Chivalry, 10: Fair play. Your answer: '))

          if choice_helping_others == 9:
              print('You chose Chivalry.\n')
              print("You're a Gryffindor!")
          elif choice_helping_others == 10:
              print("You chose Fair play.\n")
              print("You're a Hufflepuff!")
          else:
              print('Invalid choice, try again.')

      if choice_hard_work == 6:
          print("You chose Patience.\n")
          choice_patience = int(input("Choose another trait: 9: Chivalry, 10: Fair play. Your answer: "))

          if choice_patience == 9:
              print("You chose Chivalry.\n")
              print("You're a Gryffindor!")
          elif choice_patience == 10:
              print("You chose Fair play\n")
              print("You're a Hufflepuff!")
          else:
              print("Invalid choice, try again.")

      if choice_hard_work == 7:
          print("You chose Knowledge.\n")
          choice_knowledge = int(input("Choose another trait: 10: Fair play, 11: Wit. Your answer: "))

          if choice_knowledge == 10:
              print("You chose Fair play\n")
              print("You're a Hufflepuff!")
          elif choice_knowledge == 11:
              print("You chose Wit.\n")
              print("You're a Ravenclaw!")
          else:
              print('Invalid choice, try again.')


if choice_1 == 3:
    print('You chose Intelligence.\n')
    choice_intelligence = int(input('Choose another trait: 6: Patience, 7: Knowledge, 8: Cunning. Your answer: '))

    if choice_intelligence == 6:
        print("You chose Patience.\n")
        choice_patience = int(input("Choose another trait: 9: Chivalry, 10: Fair play. Your answer: "))

        if choice_patience == 9:
            print("You chose Chivalry.\n")
            print("You're a Gryffindor!")
        elif choice_patience == 10:
            print("You chose Fair play\n")
            print("You're a Hufflepuff!")
        else:
            print("Invalid choice, try again.")

    if choice_intelligence == 7:
        print("You chose Knowledge.\n")
        choice_knowledge = int(input("Choose another trait: 10: Fair play, 11: Wit. Your answer: "))

        if choice_knowledge == 10:
            print("You chose Fair play\n")
            print("You're a Hufflepuff!")
        elif choice_knowledge == 11:
            print("You chose Wit.\n")
            print("You're a Ravenclaw!")
        else:
            print('Invalid choice, try again.')

    if choice_intelligence == 8:
        print("You chose Cunning.\n")
        choice_cunning = int(input("Choose another trait: 11: Wit, 12: Resourcefulness Your answer: "))

        if choice_cunning == 11:
            print("You chose Wit.\n")
            print("You're a Ravenclaw!")
        elif choice_cunning == 12:
            print("You chose Resourcefulness.\n")
            print("You're a Slytherin!")
        else:
            print('Invalid choice, try again.')


if choice_1 == 4:
    print('You chose Ambition.\n')
    choice_ambition = int(input('Choose another trait: 5: Helping others, 7: Knowledge, 8: Cunning. Your answer: '))

    if choice_ambition == 5:
        print('You chose Helping others.\n')
        choice_helping_others = int(input('Choose another trait: 9: Chivalry, 10: Fair play. Your answer: '))

        if choice_helping_others == 9:
            print('You chose Chivalry.\n')
            print("You're a Gryffindor!")
        elif choice_helping_others == 10:
            print("You chose Fair play.\n")
            print("You're a Hufflepuff!")
        else:
            print('Invalid choice, try again.')

    if choice_ambition == 7:
        print("You chose Knowledge.\n")
        choice_knowledge = int(input("Choose another trait: 10: Fair play, 11: Wit. Your answer: "))

        if choice_knowledge == 10:
            print("You chose Fair play\n")
            print("You're a Hufflepuff!")
        elif choice_knowledge == 11:
            print("You chose Wit.\n")
            print("You're a Ravenclaw!")
        else:
            print('Invalid choice, try again.')

    if choice_ambition == 8:
        print("You chose Cunning.\n")
        choice_cunning = int(input("Choose another trait: 11: Wit, 12: Resourcefulness Your answer: "))

        if  choice_cunning == 11:
            print("You chose Wit.\n")
            print("You're a Ravenclaw!")
        elif choice_cunning == 12:
            print("You chose Resourcefulness.\n")
            print("You're a Slytherin!")
        else:
            print('Invalid choice, try again.')




# End test.