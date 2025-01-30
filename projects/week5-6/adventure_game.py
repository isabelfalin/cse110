# Title: Shadow of the Abyss

# You wake up in a dark cave, the air damp and heavy. A faint glow emanates from deep within. You don’t 
# remember how you got here, but you know one thing—you must find a way out.

# Choice 1: Where do you go?
# A) Forward – Head toward the glow.
# B) Left – Explore the darker tunnel.
# C) Right – Follow the sound of dripping water.

# If you chose A: Forward

# You step cautiously toward the glow and discover an ancient altar with a strange artifact.

# A1) Touch – Pick up the artifact.
# A2) Observe – Study it without touching.
# If you chose B: Left

# The tunnel narrows, and you hear whispers echoing in the dark.

# B1) Run – Flee before something finds you.
# B2) Listen – Stay and try to understand the whispers.
# If you chose C: Right

# You follow the sound of water and find an underground lake.

# C1) Swim – Try to cross the lake.
# C2) Wait – See if something emerges from the depths.

forward = "head towards the glow"
left = "Explore the darker tunnel"
right = "Follow the sound of dripping water"

forward_touch = "Pick up the artifact"
forward_observe = "Study it without touching"
forward_kick = "Kick the artifact"

left_run = "Flee before something finds you"
left_listen = "Stay adn try to understand the whsipers"

right_swim = "Try to cross the lake"
right_wait = "See if something emerges from the depths"

input(""" You wake up in a dark cave, the air damp and heavy. A faint glow emanates from deep within. You don't remember how you got here, 
      but you know one thing—you must find a way out.You stand up and look in front of you. You must choose a 
      passage, FORWARD, LEFT, or RIGHT. Which one do you go down? """)
if forward:
    print(f"You {forward} cautiously, and discover an ancient altar with a strange artifact. ")
else:
    print("That is not an option. Game over.")





# Title: Frozen Descent

# You're standing at the top of a towering mountain, snowboard strapped tight. The fresh snow glistens under the morning sun. The air is crisp, and the thrill of the descent awaits.

# Choice 1: Start
# A) Drop – Go straight down the steepest route.
# B) Carve – Take a slower, winding path.
# C) Jump – Launch off a nearby ridge.

# If you chose A: Drop

# You gain speed fast, the wind howling past your ears.

# A1) Brace – Steady yourself and ride it out.
# A2) Turn – Try to slow down with a sharp cut.
# If you chose B: Carve

# You glide smoothly, weaving through trees and rocks.

# B1) Push – Pick up speed and test your skill.
# B2) Ease – Keep it controlled and steady.
# If you chose C: Jump

# You soar off the ridge, adrenaline surging.

# C1) Tuck – Pull in tight for a clean landing.
# C2) Grab – Add style with a midair board grab.
# What’s your next move?

