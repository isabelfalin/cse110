print("This is a choose your own adventure titled: The Passage")

print(""" You wake up in a dark cave, the air damp and heavy. A faint glow eminates from a passage to your left, whereas to your left you hear faint whispers. You don't remember how you got here, 
      but you know one thing—you must find a way out.You stand up and look in front of you. You must choose a 
      passage, LEFT, or RIGHT. Which one do you go down? """)
action = input("> ")
if action.lower() == "left":
    print("""You head towards the faint glow and discover an ancient altar with a strange artifact. Intrigued, you reach the artifact and 
          choose whether to TOUCH it, OBSERVE it, or KICK it.""")
    action = input("> ")
else:
    print("That's not an option. Game over.")

if action.lower() == "touch":
    print("You reach out and pick up the artifact, which promptly explodes in your hands, killing you instantly")
    print("You have died. Game over.")
elif action.lower() == "observe":
    print("""You study the artifact without touching it and become mezmorized by the glow coming from within. 
          Your soul is sucked into the artifact.""")
    print("You have died. Game over.")
elif action.lower() == "kick":
    print("""You reel your leg back and strike the artifact, launching it further down the passage. As the artifact hits the ground it promptly explodes, 
          filling the tunnel with light, and illuminating another ancient alter. """)
    print("You must make a decision, do you GIVE UP or CONTINUE? ")

    action = input("> ")
if action.lower() == "give up":
    print("You give up. And stay in the tunnel forever, cold and alone. Game over.")
elif action.lower() == "continue":
    print("You continue onward and reach the new ancient alter. Atop it sits a golden dog statue. Do you PICK it up, or LOOK at it? ")

    action = input("> ")
if action.lower() == "pick":
    print("""You reach out and pick up the golden dog statue, suddnely it comes to life and licks you. the dog's lick enlightens 
          your mind, and you open your eyes, realizing it was all just a dream. You're safe. You won!!""")
elif action.lower() == "look":
    print("""You stand in front of the golden dog statue and look into it's almost lifelike eyes. Suddenly a feeling of happiness washes over you. You smile and sit on the ground, eventually, filled with joy you fall asleep. Never to wake up again.""")
    print("Game over.")
else:
    print("That's not an option. Game over.")

if action.lower() == "right":
    print("You turn down the right passage and begin walking down. As you do the passage narrows, and you hear whispers echoing in the dark. Do you RUN, or LISTEN? ")
action = input("> ")
if action.lower() == "run":
    print("Heart racing you break into a sprint and begin to run down the passage, suddenly you trip, and fall to the ground hitting your head onto the hard rock and knocking yourself out. Game over.")
elif action.lower() == "listen":
    print("You stand still and listen, trying to hear what the whispers are saying. 'give uppppp....give upppppp' they whisper. Filled with fear you turn the way you came and run towards what you think is the exit. WHen suddenly you realize it was never just a normal cave, but a great and mighty dragons cave. You run straight into his wide open mouth and are eaten. Game over. ")
else:
    print("That is not an option. Game over.")

print("Thank you for playing!")