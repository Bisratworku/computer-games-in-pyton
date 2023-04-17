import random
import time 
def gen():
    print("one or two\n")
    cave = str(random.randint(1,2))
    answer = input()
    if cave == answer:
        print("good play again")
        answer = input()
        if answer == "":
            gen()
    else:
        print("not good try again?")
        answer = input()
        if answer == "":
            cave_answer()

def cave_answer():
    print("one or two\n")
    cave = str(random.randint(1,2))
    answer = input()
    if cave == answer:
        print("good play again")
        answer = input()
        if answer == "":
            gen()
    else:
        print("not good try again?")
        answer = input()
        if answer == "":
            gen()            
cave_answer()
