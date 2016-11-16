# Our quiz!
from time import sleep
score = 0
name = ""

def quiz():
    global name
    
    print("WHAT IS YOUR NAME")
    name = input("Type Name Here: ")
    print(" Why Hello there " + name + " , do wanna play a game...")

    print("")

    sleep(2)

    print("...")

    sleep(3)

    print(".......")
    

    sleep(5)

    print("I'll take that as a yes")
    question1()

def question1():
    global score

    print("Who's the best, Bilbo or Frodo?")
    print("A. Bilbo")
    print("B. Frodo")
    answer = input("Choose one or die!")


    if answer.lower() == "a":
        score = score + 100
        print("The Hobbit Huh??")
        print(score)

    elif answer.lower() == "b":
        score = score + 200
        print("Yeah, Lord of The Rings is much better")
        print(score)
        question2()

def question2():
    global score

    print("Question 2 " + name + ", you ready?")
    sleep(1)

    print("In which movie is the name of the main character an anogram for ONE?")
    print("A. Lucy")
    print("B. The Matrix")
    print("C. War of The Worlds")
    answer2 = input("Guess")

    if answer2.lower() == "a":
        print("How is LUCY an anogram of ONE")
        print(score = score - 100)

    elif answer2.lower() == "b":
        print("Correct, NEO is an anogram for ONE")
        print(score = score + 200)

    elif answer2.lower() == "c":
        sleep(2)
        print("You dont even know his name do you?")
        answer_extra = input("YES OR NO!?")

        if answer_extra.lower() == "yes":
            print("oh,")
            sleep(1)
            print("Brownie points for you then")
            print(score = score + 50)

        elif answer_extra.lower() == "no":
            print("I KNEW IT!!!")
            print("NO MORE POINTS FOR YOU!")
            print(score = score - score)
            print("You have upset me.")
            sleep(1)
            quit()

def final_screen():
    print("This is all there is " + name)
    print("Good Bye for now")
    print("We'll be back soon")

        
            
        

        
        






# Leave this at the bottom - it makes quiz run automatically when you
# run your code.
if __name__ == "__main__":
    quiz()
