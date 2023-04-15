import random
generate_number = random.randint(0,20)
guesses = 0
for i in range(0, 20):
    print("Enter your guess number")
    input_number = input() 
    int(input_number)
    if input_number >= generate_number:
        print("Too High Try Again\n")
        guesses = guesses + 1
    elif input_number <= generate_number:
        print("Too low Try Again\n")
        guesses = guesses + 1
    elif input_number == generate_number:
        break
if input_number == generate_number:
    print("Good job it took you  " + guesses + "guesses" )