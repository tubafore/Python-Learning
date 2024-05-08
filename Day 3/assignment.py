class Game:
    def __init__(self):
        print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
        print("Welcome to Treasure Island.")
        print("Your mission is to find the treasure.") 

    def Run(self):
        print("What a lovely day for some basking in the warm sea sun, sitting by the shore, letting your feet occasionally get splashed by the waves.\n")
        print("Too bad you don't get to join in that...As the resident \"volunteer\" (this is why we don't play drinking games to lose...) your job is to explore that creepy cave over there and find the treasure!\n")
        print("Let's muster a little more enthusiasm than that...\n")
        print("As you enter the cave you see a nothing gleeming, shining, or interesting at all.  It's dark!  You walk slowly while you light your torch.  What relief!  Nice comforting light.\n")
        print("Up ahead you come to fork.  Before you can look either way, a wind comes from behind you and extinguishes your torch.  No help there.  And nothing left to light it again.\n")
        
        choice = input("You know your mission.  Find that treasure.  So what's it gonna be:  Left or Right? ")
        if (choice.lower() != "left"):
            print("\nFall into a hole.")
            print("Game Over")
            return
        else:
        
            print("\nA fine choice it turns out!  In fact, there's a little bit of light up ahead that keeps you from hitting your head again.  What?  You don't remember hitting it the first time?\n")
            print("There's gotta be a reason your head is hurting so much.\n")
            print("Ok...could be the rum.  Lousy rum...\n")
            print("NEVER MIND!  Rum is great!  Rum is super great!  (can't upset the rum now, can we?)\n")
            print("You start to hear the faint sound of flowing water.  As you walk along the path, the sound gets louder and louder until you come upon a small stream!\n")
            print("Knowing how great a swimmer you are, you could swim across it easily.  But perhaps, you should wait and think this through.  You never know what's in cave water.  Plus, it could be cold!\n")
        
            choice = input("So what's it gonna be: Swim or Wait? ")
            if (choice.lower() != "wait"):
                print("\nAttacked by a trout.")
                print("Game Over.")
                return
            else:
                print("\nUpon further reflection, it's light enough in the room to look around; no need to get wet.\n")
                print("In fact, looking around just a bit before focusing on the stream would have revealed those three doors right there.  Maybe pirates are a bit obsessed with water...\n")
                print("This seems suspicious.  Who builds doors in caves?!  Especially at the bottom of a slick stone path.  Wet rocks and time equals a slipping hazard!  But you've got to find that treasure!\n")
                print("If the slope wasn't so bad, you could probably make your way back up and try multiple, but alas...And the doors open in!  You'll slide right on through once it opens.\n")
                choice = input("Time to decide.  Do you take the Red, Blue, or Yellow door? ")
                if choice.lower() != "yellow":
                    if choice.lower() == "red":
                        print("\nBurned by fire.")
                    elif choice.lower() == "blue":
                        print("\nEaten by beasts.")
                    print("Game Over.")
                else:
                    print("\nYou Win!")
