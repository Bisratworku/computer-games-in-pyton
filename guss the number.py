import random
generate_number = random.randint(0,20)
guesses = 0
print(generate_number)
for i in range(0, 25):
    print("Enter your guess number")
    input_number = input()
    input_number = int(input_number) 
    int(input_number)
    if input_number > 20:
         print("You must insert the number between 0 and 20")
    elif input_number > generate_number:
            print("Too High Try Again\n")
            guesses = guesses + 1
    elif input_number < generate_number:
        print("Too low Try Again\n")
        guesses = guesses + 1
    elif input_number == generate_number:
        guesses = str(guesses)
        print("Good job it took you  " + guesses + " guesses" )
        break
    