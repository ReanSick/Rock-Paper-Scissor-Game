import turtle
import random


# screen
#win = turtle.Screen()
# win.title("PKT")
# in.bgpic("low-tier-god.gif")
#win.setup(width=800, height=600)
# win.tracer(0)

# divider
#div = turtle.Turtle()
#div.speed(0)
#div.shape('square')
#div.color('pink')
#div.shapesize(stretch_wid=5, stretch_len=1)

#div.goto(350, 0)


print("Welcome you playin?")
ans = input(" ")

if ans.lower() == "yes":
    print("Welcome to PKT")
    print("------------------------------------------")
    print("Rules are simple You have 3 options; \n Punch \n Kick \n Throw \n Just like a fighting game.")
    print("Punch beats Kick")
    print("------------------------------------------")
    print("Throw beats Punch")
    print("------------------------------------------")
    print("Kick beats Throw")
    print("------------------------------------------")
    print("Lets Play")
    print("------------------------------------------")
    print("Added  DLC: Fireball, Sidestep, Air Dash, Parry, and Block")
    print("------------------------------------------")
    # game Loop
    while True:
        action = input(
            "Enter your move: Punch, Kick, Throw, Fireball, Air Dash, Parry, or Block ")
        print("------------------------------------------")
        pos_act = ["Punch", "Kick", "Throw",
                   "Fireball", "Air Dash", "Parry", "Block"]
        cpu2 = random.choice(pos_act)
        print(f"You choose {action}: The CPU chose {cpu2}")
        print("------------------------------------------")

        if action == cpu2:
            print(f"You both chose the same action: Back to neutral")
            print("------------------------------------------")

        elif action == "Punch":
            if cpu2 == "Throw":
                print("Get that azz grabbed: You Lost")
                print("------------------------------------------")

            else:
                print("Nice Punch lookin like Dudley: You Win")
                print("------------------------------------------")

        elif action == "Kick":
            if cpu2 == "Punch":
                print("Get that azz punched: You Lost")
                print("------------------------------------------")

            else:
                print("Nice Kick lookin like Chun-Li: You Win")
                print("------------------------------------------")

        elif action == "Throw":
            if cpu2 == "Kick":
                print("Get that azz kicked: You Lost")
                print("------------------------------------------")

            else:
                print("Nice Throw lookin like Potemkin: You Win")
                print("------------------------------------------")

        elif action == "Fireball":
            if cpu2 == "Block":
                print("Get that azz Blocked: You Lost")
                print("------------------------------------------")
            else:
                print("Nice Fireball lookin like Ryu: You Win")
                print("------------------------------------------")

        elif action == "Parry":
            if cpu2 == "Block":
                print("2 defensive minded players")
                print("Boring")
                print("------------------------------------------")
            elif cpu2 == "Throw":
                print("Get that azz thrown: You Lost")
                print("------------------------------------------")
            else:
                print("Nice Parry lookin like Diago: You win")

        elif action == "Block":
            if cpu2 == "Air Dash":
                print("Get that azz read: You Lost")
                print("------------------------------------------")
            elif cpu2 == "Parry":
                print("2 defensive minded players")
                print("Boring")
            else:
                print("Nice Block: You win")

        # end of game loop and replay
        print("Nice combo :D")
        play_again = input("Again?: (y/n): ")
        print("------------------------------------------")
        if play_again == "y":
            print("Big Ups")
        else:
            print("Probaly was a Scrub anyway")
            break
        # score wont go past 1 no amount of googling will help me
else:
    print("Blocked")
