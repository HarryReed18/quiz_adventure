# An adventure game
from time import sleep
health = 0
enemy_health = 0
karma = 0
def into():

     
     global health
     global enemy_health
     global karma
    
   

def room1():

    
    global health
    global enemy_health
    global karma

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
        print("You lift the cloth to find that the source of the creature is simply just as terrified as  you and is squealing in terror")
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
        print(karma = karma - 5)
        sleep(5)

        room2()

def room2():
    
    global health
    global enemy_health
    global karma
    
    
    
        
        








# Leave this at the bottom - it makes room1 run automatically when you
# run your code.
if __name__ == "__main__":
    room1()
