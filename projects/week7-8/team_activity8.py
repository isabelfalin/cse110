# favorite_letter = input("What is your favorite letter? ")
# my_word = "hello"
# for letter in my_word:
#     if letter == favorite_letter:
#         print(favorite_letter.upper())
#     else:
#         print(favorite_letter.lower())

# favorite_letter = input("What is your favorite letter? ")

# word = "commitment"
# for letter in word:
#     if letter == favorite_letter.lower():
#         print("_", end="")
#     else: 
#         print(f"{letter}".lower(), end="")
# print()
        

quote = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."


play_game = "yes"

while play_game == "yes":
    number = int(input("Please enter a number: "))

    for p, letter in enumerate(quote):
        if p % number == 0:
            print(f"{letter}".upper(), end="")
        else: 
            print(f"{letter}".lower(), end="")

    print("\n")
    play_game = input("Would you like to use a different number? (y/n) ")



   