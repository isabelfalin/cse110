friends = []

their_friend = input("Type the name of a friend(end to end): ")
while their_friend.lower() != "end":
    friends.append(their_friend)
    their_friend = input("Type the name of a friend (end to end): ")


for friend in friends:
    print(friend)


