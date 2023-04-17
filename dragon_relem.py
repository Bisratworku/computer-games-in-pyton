import random
import time 

def gen():
    print("You are infront of two huge caves both have dragons inside but one of the dragon is friendly so it will give you tons of gold and the other is evil you need to choose between the cave one and two  \n")
    cave = str(random.randint(1,2))
    answer = input()
    time.sleep(2)
    print("you are approching the cave\n")
    time.sleep(2)
    if cave == answer:
        print("You got the gold congragulations PRESS ENTER to play again")
        answer = input()
        if answer == "":
            gen()
    else:
        print("YOU died PRESS ENTER try again?")
        answer = input()
        if answer == "":
            gen()

def cave_answer():
    print("You are infront of two huge caves both have dragons inside but one of the dragon is friendly so it will give you tons of gold and the other is evil you need to choose between the cave one and two  \n")
    cave = str(random.randint(1,2))
    answer = input()
    time.sleep(2)
    print("you are approching the cave\n")
    time.sleep(2)
    if cave == answer:
        print("You got the gold congragulations PRESS ENTER to play again")
        answer = input()
        if answer == "":
            gen()
    else:
        print("YOU died PRESS ENTER try again?")
        answer = input()
        if answer == "":
            gen()            
cave_answer()
