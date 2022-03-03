# CS 232 Spring 2022 - Week 07 Lab
# Sarah Jimenez and Trever Sieger and My Sou

import random

# Craps Game

# Part 1

def dice_roller():
    
    while True:
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        
        yield dice1 + dice2


# Part 2

roll_dice = dice_roller()
next(roll_dice)

# Part 3

def play_craps():
    
    first_roll = next(roll_dice)
    # print("You rolled a ", first_roll)
    
    if first_roll == 7 or first_roll == 11:
        # print("You win")
        return True
    
    elif first_roll in [2, 3, 12]:
        # print("You lose")
        return False
    
    else:
        point = first_roll
        keep_rolling = True
        
        while keep_rolling:
            next_roll = next(roll_dice)
            # print("next roll is ", next_roll)
            
            if next_roll in [point, 7]:
                keep_rolling = False
                
                if next_roll == point:
                    return True
                
                elif next_roll == 7:
                    return False


# Part 4

def run_trials(games_to_play):
    
    games_won = 0
    games_lost = 0

    for game in range(1, games_to_play +1):
        if play_craps() == True:
            games_won += 1

        else:
            games_lost += 1

    stats = round((games_won * 100 / games_to_play), 2)
    
    print("Out of {} games, you won {} and lost {}"
          .format(games_to_play, games_won, games_lost))
    
    print("Winning percent is {}%".format(stats))

    # After running a million games, it was just under 50% wins
    # so you should bet for pass to lose
    
