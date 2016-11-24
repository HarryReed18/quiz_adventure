# An adventure game









 







from random import randint
from time import sleep
health = 20
enemy_health = 0
karma = 0
def intro():

     
     global health
     global enemy_health
     global karma

def status_bar():
     global health, karma

     print(""*5)
     print("===================================")
     print("   HP", health,"  Karma", karma)
     print("===================================")
     print("")
     
def remove_HP(hp, prompt):
     global health

     health = health - hp
     print("You lose", hp, "health")
     print(prompt)
     if health <= 0:
          print("Game Over")
          quit()
    
   

def room1():

    
    global health
    global enemy_health
    global karma

    

    status_bar()



    print("You wake up, lost and alone in a dark moving prison with no memory of how you got there")
    sleep(2)
    print("your memory is blurry and the only thing you remember is a woman screaming at you as you're being pulled away")
    sleep(1)
    print("Wait...")
    sleep(3)
    print("Who was it")

    print("Contemplating your life and waiting for the prison to stop,  you suddenly hear a horrific roar emerge from underneath a dusty grey cloth") 
    print("What do you do?")
    sleep(1)
    print("A, Quench your curiosity and remove the cloth")
    sleep(1)
    print("B. Be a man and kill the beast!!")
    sleep(1)
    answer = input("???????- ")

    if answer.lower() == "a":
        print("You lift the cloth to find that the source of the sound is mearly a creature just as terrified as  you and is squealing in terror")
        sleep(2)
        print("You feel symapthy for the creature and calm it down")
        sleep(1)
        print("After looking around for a short while you find some stale bread and share it with the creature")
        karma = karma + 10
        print("Karma: ", karma )

    elif answer.lower() == "b":
        print("You see a lighter in the corner of your eye and set the suprisingly flamable cloth on fire")
        sleep(1)
        print("You curl up in a ball in the center of the floor and cry as the creature cries out in agony as it slowly burns to death")
        print("as it burns you cant help but begin to feel hungry...")
        karma = karma - 5
        print("Karma: ", karma )
        sleep(5)

        room2()

def room2():
    
    global health
    global enemy_health
    global karma

    status_bar()

    print("Hours pass...")
    sleep(2)
    print("A sudden jolt of movement startles you as the moving cell accelerates towards the top of nothing...")
    sleep(1)
    print("You have little time until the cell is crushed on the top of the shaft")
    print("A. Lie on the floor and hope you dont get crushed")
    print("B. Tear a gurder from the cell and jam it between the walls of the shaft and the cell to slow it down")
    print("C. Use a spell to stop the cell")
    answer = input("Quickly you dont have much time- ")

    if answer.lower() == "a":
        print("You lie on the floor waiting for the cell to be crushed at the top of the shaft")
        sleep(2)
        print("You can see the top now, but only just")
        sleep(1)
        print("You can make out a sliver a light piercing through the centre of the ceiling")
        sleep(1)
        print("As you get closer to the top you notice the sliver of light is getting bigger and bigger")
        print("It's an opening!")
        sleep(1)
        print("when the cell reaches the top it flighs off of its supports into the air")

    elif answer.lower() == "b":
          print("You seriosly think you're that strong?")

          remove_HP(1,)
          
          sleep(2)
          print("The gods respect your courage")
          karma = karma + 5
          print("karma:" ,karma)

    elif answer. lower() == "c":
          print("...")
          sleep(2)
          print("I want to make this perfectly clear")
          sleep(2)
          print("Magic")
          sleep(1)
          print("IS NOT IN THIS GAME")

          

          
          
    
    
    
        
        








# Leave this at the bottom - it makes room1 run automatically when you
# run your code.
if __name__ == "__main__":
    room1()

    





