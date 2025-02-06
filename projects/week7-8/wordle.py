# Have a secret word stored in the program.

# Prompt the user for a guess.

# Continue looping as long as that guess is not correct.

# Calculate the number of guesses and display it at the end.

# You do not need to have any hints at this point.

# secret_word = "elephant".lower()
# guess = None 
# counter = 0
# while guess != secret_word:
#     guess = input("What is your guess? ").lower() 
#     counter = counter + 1
#     if guess == secret_word:
#         print(f"You guessed it! It took you {counter} guesses!")
#     else:
#         print("Your guess is not correct.")


secret_word = "monkey"
guess = input(f"Give me a {len(secret_word)} letter word: ").lower()
print(f"Comparing {secret_word} and {guess}.")

if (len(guess)) == (len(secret_word)):
    for position in range(len(secret_word)):
        guess_letter = guess[position]
        same_position = guess_letter == secret_word[position]
        found_in_word = guess_letter in secret_word
        if same_position:
            print(f"{guess_letter} is at the same position as both words")
        elif found_in_word:
            print(f"{guess_letter} is in the word but not at this position")
        else:
            print(f"{guess_letter} is not found in the word")
else:
    print(f"that was NOT a {len(secret_word)} letter word!")

