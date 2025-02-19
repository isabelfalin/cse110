
chapters_largest = 0
answer = input("What scriptures would you like to learn about? ")

with open("books_and_chapters.txt") as book_file:
    for info in book_file:
        split_person = info.strip().split(":")
        book = split_person[0]
        chapters = int(split_person[1])
        scripture = split_person[2].lower()

        if answer.lower() == scripture:
                print(f"Scripture: {scripture.title()}, Book: {book.title()}, Chapters: {chapters}")
                if chapters > chapters_largest:
                    chapters_largest = chapters
                    biggest_book = book
                        
    print()
    print(f"The book with the largest number of chapters is: {biggest_book}")
    print(f"The largest number of chapters in the scriptures is: {chapters_largest}")
# print()
# print(f"The youngest person is {youngest_name}, they are {youngest_age} years old.")
