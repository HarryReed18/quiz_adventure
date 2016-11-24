# An adventure game
from random import randint
from time import sleep

player_damage_with_stick = randint(3, 10)
player_damage = randint(1, 8)

enemy_damage = randint(1, 5)
stick = 0



def combat_screen():

            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("                                  Fighting...                                ")
            print("     YOU MUST HIT ABOVE A FIVE TO KILL THE SPIDER       ")
            print("   IF THE SPIDER HITS HIGHER THAN YOU, YOU WILL DIE    ")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def game_over():
            print("~~~~~~~~~~~~") 
            print("  GAME  OVER   ")
            print("~~~~~~~~~~~~")

def combat_code():
                print("You only have a stick to fight with!")
                print("You swiftly jab the spider in one of it's eye's to gain an advantage")
                sleep(2)
                combat_screen()            
                sleep(2)

                print("You hit a", player_damage_with_stick)
                sleep(1)
                print("The spider hits a", enemy_damage)

                if player_damage_with_stick < enemy_damage:
                    print("The spider has dealt more damage than you!")
                    print("You fall to the floor in a dramatic scene of pain and die")
                    print("The spider lays it's eggs in your corpse")

                    game_over()

                elif player_damage_with_stick < 5:
                    print("You didnt deal enough damage to kill the spider, but manage to escape")

                else:
                    print("Yoy have killed the spider!")








            

def room1():
        global player_damage, enemy_damage,  stick

        print("~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(" Welcome to Lost Cavern of Secrets! ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~")

        sleep(3)

        print("You enter a dark cavern out of curiosity, it is ominus and mysterious.")
        sleep(1)
        print("At the enterance of the cavern you can make out a wooden stick")
        sleep(1)
        answer = input("Do you take it? [y/n]:")
#stick taken
        if answer.lower() == "y":
            print("You have taken the stick!")
            print("You stuff it in your backpack for safe keeping")
            sleep(1)
            stick = stick + 1
            print("You now have ", stick, "sticks")
            
#stick not taken
        elif answer.lower() == "n":
            print("You thought it best to leave the majestic stick and enter the cave without a second thought")
            print("What could possibly go wrong?")

            sleep(2)

        room2()

            
def room2():
        global player_damage, enemy_damage, stick

        print("As you proceed deeper into the cave, you see a small object emitting light")
        answer = input("Approach the object? [y/n]:")
#approach Spider
        if answer.lower() == "y":
            print("You cautiously sneak towards the object...")
            sleep(2)
            print("As you draw closer, you begin to realise that the object is an eye!")
            sleep(1)
            print("You start to panic and breath heavily as the object sprouts more and more eyes!")
            print("2")
            print("4")
            print("8")
            sleep(1)
            print("It's a Spider!!")
            sleep(1)
            print("There is little time")
            answer = input("Do you fight it? [y/n]:")
#fight spider
        if answer.lower() == "y":
            #with stick
            
            if stick == 1:
                print("You only have a stick to fight with!")
                print("You swiftly jab the spider in one of it's eye's to gain an advantage")
                sleep(2)
                combat_screen()            
                sleep(2)

                print("You hit a", player_damage_with_stick)
                sleep(1)
                print("The spider hits a", enemy_damage)

                if player_damage_with_stick < enemy_damage:
                    print("The spider has dealt more damage than you!")
                    print("You fall to the floor in a dramatic scene of pain and die")
                    print("The spider lays it's eggs in your corpse")

                    game_over()

                elif player_damage_with_stick < 5:
                    print("You didnt deal enough damage to kill the spider, but manage to escape")

                else:
                    print("Yoy have killed the spider!")
#without stick
        elif:
            print("You dont have anything to fight with!")
            sleep(2)

            
            combat_screen()

            sleep(2)
            print("You hit for", player_damage)
            print("The spider hits for", enemy_damage)
            sleep(1)

            combat_code()


        #dont fight the spider
        else:
            print("You turn away from the spider and run as fast as you can")
            sleep(1)
            print("As you get closer to the exit of the cavern everything begins to crumble around you")
            sleep(2)
            print("The walls fall away and the floor disappears")
            sleep(3)
            print("Infront of you are two red velvet arm chairs infront of a fireplace")
            sleep(2)
            print("You approach the chairs and realise there is a man with a long black coat and sunglasses on sitting in one")
            sleep(1)
            print("He turns to face you and asks")
            sleep(3)
            print("This is your last chance")
            print("After this there is no turning back")
            print("The red pill")
            sleep(1)
            print("or")
            sleep(1)
            print("The blue pill")
            sleep(4)

        game_over()

        sleep(2)

        quit()
            
       
            
            
                    

                    

                
                
            
            
        
        


        
          

          

          
          
    
    
    
        
        








# Leave this at the bottom - it makes room1 run automatically when you
# run your code.
if __name__ == "__main__":
    room1()

    





