guess=int(input("Guess a number : "))
while guess != 10 :
    print("You guessed the wrong answer")
    guess=int(input("Guess another number : "))
print(f"You guessed the correct answer : {guess}") 