import random

def main():
    print("Round 1!")
    x = random.randint(2,13)
    print ("You have drawn " + str(x))
    y = random.randint(2,13)
    print ("Opponent has drawn " + str(y))

    if x == 21:
        print ("You have won!")
    elif x > 21:
        print ("You have lost...")
    elif y == 21:
        print ("Opponent has drawn " + str(y))
        print ("You have lost...")
    elif y > 21:
        print ("Opponent has drawn " + str(y))
        print ("You have won!")
    else:
        print("Round 2")
        turn2 = input("Contine? :")
        if turn2 == "y":
            x = x + random.randint(2,13)
            print ("You have drawn " + str(x))
            y = y + random.randint(2,13)

            if x == 21:
                print ("You have won!")
            elif x > 21:
                print ("You have lost...")
            elif y == 21:
                print ("Opponent has drawn " + str(y))
                print ("You have lost...")
            elif y > 21:
                print ("Opponent has drawn " + str(y))
                print ("You have won!")
            else:
                print("Round 3")
                turn3 = input("Contine? :")
                if turn3 == "y":
                    x = x + random.randint(2,13)
                    print ("You have drawn " + str(x))
                    y = y + random.randint(2,13)
                
                if x > 21:
                    print ("You have lost...")
                elif y == 21:
                    print ("Opponent has drawn " + str(y))
                    print ("You have lost...")
                elif y > 21:
                    print ("Opponent has drawn " + str(y))
                    print ("You have won!")
                else:
                    y = y + random.randint(2,13)
                    if (y > x) and y < 21:
                        print ("Opponent has drawn " + str(y))
                        print ("You have lost...")
                    elif y > 21:
                        print ("Opponent has drawn " + str(y))
                        print ("You have won!")
         

        else:
            y = y + random.randint(2,13)
            if y < 21:
                print ("Opponent has drawn " + str(y))
                print ("You have lost...")
            elif y > 21:
                print ("Opponent has drawn " + str(y))
                print ("You have won!")

    Repeat = input("Play Again? :")
    if Repeat == "y":
        main()
    else:
        print("Loser")
        exit()
main()
       

