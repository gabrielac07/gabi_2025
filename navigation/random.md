---
layout: post
title: Random Simulation
permalink: /random/
---
## Popcorn Hack 1: Real-World Applications

Cybersecurity (e.g., password generation and encryption):
Random numbers are critical for creating secure passwords, cryptographic keys, and tokens. Without true randomness, systems would be vulnerable to hacking and unauthorized access.

Video Games (e.g., loot drops or enemy behavior):
Random number generation makes games more exciting and unpredictable. For example, it can determine what loot a player gets or how enemies behave, adding variety and replayability.

## Popcorn Hack 2: Magic 8-Ball with Run Button

```python
import random

def magic_8_ball():
    num = random.random()
    if num < 0.5:
        return "Yes"
    elif num < 0.75:
        return "No"
    else:
        return "Ask again later"

# Test your function
for i in range(10):
    print(f"Magic 8-Ball says: {magic_8_ball()}")
```

## Popcorn Hack 3: # Modified traffic light simulation


```python
states = ["Green", "Yellow", "Red"]
durations = {"Green": 5, "Yellow": 2, "Red": 4}
timeline = []

# Simulate 20 time steps
time = 0
state = "Green"
counter = 0

while time < 20:
    timeline.append((time, state))
    counter += 1
    if counter == durations[state]:
        counter = 0
        current_index = states.index(state)
        state = states[(current_index + 1) % len(states)]
    time += 1

for t, s in timeline:
    print(f"Time {t}: {s}")
```

### Reflection:
This is a simulation because it models how a real-world traffic light system operates over time using rules and time steps. Its real-world impact lies in helping city planners or engineers test timing sequences and improve traffic flow efficiency without needing to test on actual roads.

## Homework Hack 1: Dice Game simulation


```python
import random

def roll_dice():
    """Roll two dice and return their values and sum."""
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    print(f"Rolled: {die1} + {die2} = {total}")
    return total

def play_dice_game():
    """
    Play one round of the dice game.
    Returns True if player wins, False if player loses.
    """
    first_roll = roll_dice()

    if first_roll in [7, 11]:
        print("You win!")
        return True
    elif first_roll in [2, 3, 12]:
        print("You lose!")
        return False
    else:
        point = first_roll
        print(f"Point is set to {point}. Keep rolling!")

        while True:
            roll = roll_dice()
            if roll == point:
                print("You hit the point! You win!")
                return True
            elif roll == 7:
                print("Rolled a 7. You lose!")
                return False

def main():
    """Main game function with game loop and statistics."""
    wins = 0
    losses = 0

    while True:
        play = input("\nDo you want to play? (yes/no): ").strip().lower()
        if play == "yes":
            if play_dice_game():
                wins += 1
            else:
                losses += 1
            print(f"\nCurrent Stats: {wins} Wins, {losses} Losses")
        elif play == "no":
            print(f"\nFinal Stats: {wins} Wins, {losses} Losses")
            print("Thanks for playing!")
            break
        else:
            print("Please enter 'yes' or 'no'.")

print("Welcome to the Dice Game!")
main()
```
