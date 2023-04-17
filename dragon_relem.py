import random
import time
def generate_input():
    print("You are infront of to dragon caves in one cave their is a friendly dragon that will give you gold in other their is a dragon that will tear you apart and kill you you must choose one of the two choose wisely 1 or 2 ")
    choosen_cave = input()
    return choosen_cave
def generate_cave():
    cave = random.randint(1,2)
    return cave

