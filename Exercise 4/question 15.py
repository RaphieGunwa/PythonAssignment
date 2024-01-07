import random

def roll_dice_until_seven():
    random_generator = random.Random()
    total_rolls = 0
    
    while True:
        roll1 = random_generator.randint(1, 6)
        roll2 = random_generator.randint(1, 6)
        total_rolls += 1
        print(f"{roll1} + {roll2} = {roll1 + roll2}")
        
        if roll1 + roll2 == 7:
            print(f"You won after {total_rolls} tries!")
            break

roll_dice_until_seven()
