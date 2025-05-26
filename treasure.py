# Je gaat een nieuw programma schrijven, genaamd treasure.py. Dit programma is een spel waarbij de speler een aantal keuzes moet maken.
# Je mag zelf bepalen wat de keuzes zijn en wat de uitkomsten zijn van de keuzes. Het spel moet minimaal 4 verschillende keuzes bevatten.
# Het einde van het spel is een if elif else statement.
#
# Voorbeeld:
# Welkom op het eiland van de schat.
# Je bent op een kruispunt, ga je links of rechts?
# Rechts
#  Helaas heb je verkeerd gekozen en ben je in een gat gevallen. Game Over.
#
# Of:
# Welkom op het eiland van de schat.
# Je bent op een kruispunt, ga je links of rechts?
# Links
# Je komt bij een meer, ga je zwemmen of wachten?
# etc...

print("""
                  __..-----')
        ,.--._ .-'_..--...-'
       '-"'. _/_ /  ..--''""'-.
       _.--""...:._:(_ ..:"::. \\
    .-' ..::--""_(##)#)"':. \\ \\)    \\ _|_ /
   /_:-:'/  :__(##)##)    ): )   '-./'   '\\.-'
   "  / |  :' :/""\\///)  /:.'    --(       )--
     / :( :( :(   (#//)  "       .-'\\.___./'-.
    / :/|\\ :\\_:\\   \\#//\\            /  |  \\
    |:/ | ""--':\\   (#//)              '
    \\/  \\ :|  \\ :\\  (#//)
         \\:\\   '.':. \\#//\\
          ':|    "--'(#///)
                     (#///)
                     (#///)         ___/""\\     
                      \\#///\\           oo##
                      (##///)         `-6 #
                      (##///)          ,'`.
                      (##///)         // `.\\
                      (##///)        ||o   \\\\
                       \\##///\\        \\-+--//
                       (###///)       :_|_(/
                       (sjw////)__...--:: :...__
                       (#/::''':::     "" - -.._
                  __..-'''           __;: :            "-._
          __..--""                  `---/ ;                '\\._
 ___..--""                             `-'                    "-..___
   (_ ""---....___                                     __...--"" _)
     ""--...  ___""'''-----......._______......----""'     --""
                          ---.....   ___....----             
""")


# Schrijf hier je code:

print('You went on vacation. You have overheard that there is a treasure on this island. You go and search for it.\n')
print('Which way to you go?')
choice_1 = int(input('1: North, 2: East, 3: South, 4: West.\nYour answer (Choose a number.): \n'))

#Choice north
if choice_1 == 1:
    print('You went North. You walked into the swamp and were attacked by alligators. Game over.\n')

#Choice east
elif choice_1 == 2:
    print('You went East. You see a group of people native to the island.')

    # Choice talk to people
    choice_east = int(input('Talk to the people? 5: Yes. 6: No.\nYour answer (Choose a number.):\n'))
    # Talk to people
    if choice_east == 5:
        print('You talked to the people. They don\'t understand your language and think you are a threat, they chase you down with spears and kill you. Game Over.')
    # Don't talk to people
    elif choice_east == 6:
        print('You didn\'t talk to the people. Good idea, because when you kept walking you saw a pile of human bones.')

        # Choice dig through bones.
        choice_bones = int(input('Dig through the bones? 7: Yes. 8: No.\nYour answer (Choose a number.):\n'))
        # Dig bones
        if choice_bones == 7:
            print('You dug through the bones.')

            # Choice amulet
            choice_amulet = int(input('You found an amulet. It\'s leading you to a nearby cave. Go to the cave? 9: Yes. 10: No.\nYour answer (Choose a number.):\n'))
            # Grab amulet
            if choice_amulet == 9:
                print('You walk to the cave.')

                # Choice cave
                choice_cave = int(input('You entered the cave and find a shovel. Where do you dig? 11: Near the river. 12: Inside the cave. 13: Go back to the people.\nYour answer (Choose a number.):\n'))
                # Dig river
                if choice_cave == 11:
                    print('You went to dig near the river. You disturbed a giant anaconda and it decided to make you it\'s meal. Game Over')
                # Dig in cave
                elif choice_cave == 12:
                    print('You dug inside of the cave! Congratulations! You found the treasure! You win!')
                    print("""
                                          __..-----')
                                ,.--._ .-'_..--...-'
                               '-"'. _/_ /  ..--''""'-.
                               _.--""...:._:(_ ..:"::. \\
                            .-' ..::--""_(##)#)"':. \\ \\)    \\ _|_ /
                           /_:-:'/  :__(##)##)    ): )   '-./'   '\\.-'
                           "  / |  :' :/""\\///)  /:.'    --(       )--
                             / :( :( :(   (#//)  "       .-'\\.___./'-.
                            / :/|\\ :\\_:\\   \\#//\\            /  |  \\
                            |:/ | ""--':\\   (#//)              '
                            \\/  \\ :|  \\ :\\  (#//)
                                 \\:\\   '.':. \\#//\\
                                  ':|    "--'(#///)
                                             (#///)
                                             (#///)         ___/""\\     
                                              \\#///\\           oo##
                                              (##///)         `-6 #
                                              (##///)          ,'`.
                                              (##///)         // `.\\
                                              (##///)        ||o   \\\\
                                               \\##///\\        \\-+--//
                                               (###///)       :_|_(/
                                               (sjw////)__...--:: :...__
                                               (#/::''':::     "" - -.._
                                          __..-'''           __;: :            "-._
                                  __..--""                  `---/ ;                '\\._
                         ___..--""                             `-'                    "-..___
                           (_ ""---....___                                     __...--"" _)
                             ""--...  ___""'''-----......._______......----""'     --""
                                                  ---.....   ___....----             
                        """)
                # Go back to people
                elif choice_cave == 13:
                    print('You go back to the people. They appreciate the gift of the shovel. You don\'t die but you also have not found the treasure. Game Over.')
                else:
                    print('Invalid choice, try again.')

            # Don't grab amulet
            if choice_amulet == 10:
                print('Hundreds of venomous spiders crawl out of the bones and swarm you. Game Over.')
            else:
                print('Invalid choice, try again.')

        # Don't dig bones.
        if choice_bones == 8:
            print('The people saw you lingering by their pile of bones and chased you with spears. Game over.')

        else: print('Invalid choice, try again.')

    else:
        print('Invalid choice, try again.')

#Choice south
elif choice_1 == 3:
    print('You went South. You weren\'t paying attention and you fell into a ravine.')

elif choice_1 == 4:
    print('You went West and entered a saloon. The cowboys shot you for trespassing.')

else: print('Invalid choice, try again.')
