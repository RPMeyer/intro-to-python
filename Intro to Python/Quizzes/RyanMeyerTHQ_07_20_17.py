import random

def roll_dice():
    '''rolls fair 6 sided dice using random int (times) times'''
    diceRoll = random.randint(1,6)
    return diceRoll
#
# for i in range(20):
#     print(roll_dice(), end = ' ')

def roll_dice_repeat(n):
    diceRollList= []
    for i in range(n):
        diceRollList.append(roll_dice())
    return diceRollList

# dice_rolls = roll_dice_repeat(5)
# print(dice_rolls)

def points_of(dice_rolls):
    '''returns points for a dice_roll of 1,2,3,4,5, or 6'''
    gamePoints = {1:10,2:9,3:8,4:7,5:6,6:5}

        # gameScore= 0
        # for i in dice_rolls:
        #     gameScore = gameScore + gamePoints[i]

    return gamePoints[dice_rolls]

def score_dice(dice_rolls):
    '''returns the game score of the list dice_rolls'''
    gameScore= 0
    for i in dice_rolls:
        gameScore = gameScore + points_of(i)
    return gameScore

for i in range (1,7):
    print("{} is worth {}".format(i, points_of(i)))

dice_rolls = roll_dice_repeat(8)
game_score = score_dice(dice_rolls)
print(game_score)
