#intro to programming
#author: susan cantoni
#date: 02-26-18
#guessing game

animal = "lion"

def main():
    print("I am thinking of an animal...")
    guess = input("What am I thinking of? ")
    correct = False
    while not correct:
        if guess != 'lion':
            print ("Wrong answer! Guess again.")
            guess = input("What am I thinking of? ")
        else:
            print ("Congratulations! You got it!")
            return

main()
