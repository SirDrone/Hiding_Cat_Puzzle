#!/usr/bin/env python3

from cat_puzzle import Cat_Puzzle

#Run the puzzle program
if __name__ == '__main__':

    #Values you can change:
    player_mode = "absurd" #You can change this value between 'absurd', 'debug', or 'custom'
    total_boxes = 5 #You can also change this value to a number greater than 2.  I recommend 5 or 7 for scale
    verbose = True #You can also change this value between True and False

    #Now to begin the game based on our choices:
    if verbose:
        print("Welcome to the Cat Puzzle game!  This challenge stems from a Microsoft interview riddle.\n" \
                "The puzzle is simple.  There is a cat who loves boxes, and you, as the player, " \
                "get a prize for picking the box with the cat in it.\n" \
                "However, each day, the cat will move to an adjacent box, " \
                "and the owner only lets you pick one box per day, with a small fee charged each day you play.\n" \
                "What strategies can you use to find the cat and win the prize consistently in the fewest number of days, and minimize the overall toll?\n")

    #The absurd mode automatically sets up a worst-case scenario game (but only for 5 boxes, feel free to change that)
    if player_mode == "absurd":
        puzzle = Cat_Puzzle(mode='A', total_boxes=total_boxes, verbose=verbose)

    #The debug mode will allow for a play-by-play analysis of what's happening in absurd mode.  
    #Consider having verbose=True as well to more fully utilize it
    elif player_mode == "debug":
        puzzle = Cat_Puzzle(mode='A', total_boxes=total_boxes, debug=True, verbose=verbose)
        game_not_solved = True
        while game_not_solved:
            game_not_solved = puzzle.take_turn(verbose=verbose)
            if verbose:
                print(puzzle.get_stats())

    #This mode allows you to customize everything from the command-line
    elif player_mode == "custom":
        puzzle = Cat_Puzzle()
