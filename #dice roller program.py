#dice roller program

import random
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
# ● ┌ ─ ┐ │ └ ┘ sq-art

#"┌───────┐"
#"│       │"
#"│       │"
#"│       │"
#"└───────┘"

dice_art = {
    1: ["┌───────┐", 
        "│       │", 
        "│   ●   │", 
        "│       │", 
        "└───────┘"],
    2: ["┌───────┐", 
        "│ ●     │", 
        "│       │", 
        "│     ● │", 
        "└───────┘"],
    3: ["┌───────┐", 
        "│ ●     │", 
        "│   ●   │", 
        "│     ● │", 
        "└───────┘"],
    4: ["┌───────┐", 
        "│ ●   ● │", 
        "│       │", 
        "│ ●   ● │", 
        "└───────┘"],
    5: ["┌───────┐", 
        "│ ●   ● │", 
        "│   ●   │", 
        "│ ●   ● │", 
        "└───────┘"],
    6: ["┌───────┐", 
        "│ ●   ● │", 
        "│ ●   ● │", 
        "│ ●   ● │", 
        "└───────┘"]
}

while True:
    dice = []
    total = 0
    num_of_dice = int(input("How many dice do you want to roll? "))

    for die in range(num_of_dice):
        die = random.randint(1, 6)
        dice.append(die)

    for line in range(5):
        for die in dice:
            print(dice_art.get(die)[line], end="")
        print()

    for die in dice:
       total += die
    print(f"total: {total}")
    print("Thank you for playing!")