import random

word_list = ["elephant", "juice", "house", "bacon", "temple", "soccer", "snowboarding", "supercalifragilisticexpialidocious"]

# Setup the game
secret_word = random.choice(word_list)
counter = 0
guess = None

# print the hint
print("Your hint is: ", end="")
for letter in secret_word:
    print("_ ", end="")

print("\n")

# Start the game loop
while guess != secret_word:
    counter = counter + 1

    # Get guess
    guess = input("What is your guess? ").lower() 

    # check guess length
    if len(guess) != len(secret_word):
        print(f"Sorry, the guess must have {len(secret_word)} letters.\n")
        continue
    
    # Check guess
    if guess == secret_word:
        print(f"You guessed it! It took you {counter} guesses!")
    else:
        print("Your guess is not correct.")

        # Print the new hint
        print("Your hint is: ", end="")

        for position in range(len(secret_word)):

            guess_letter = guess[position]
            secret_letter = secret_word[position]
            
            if guess_letter == secret_letter:
                same_position = True
            else:
                same_position = False
            
            found_in_word = guess_letter in secret_word

            if same_position:
                print(f"{guess_letter.upper()} ", end="")
            elif found_in_word:
                print(f"{guess_letter.lower()} ", end="")
            else:
                print("_ ", end="")

        print("\n")
