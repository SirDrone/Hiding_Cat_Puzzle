#!/usr/bin/env python3

from hiding_cat_puzzle import Cat_Puzzle

#Run the puzzle program
if __name__ == '__main__':

    #Values you can change:
    player_mode = "absurd" #You can change this value between 'absurd', 'debug', or 'custom'
    total_boxes = 5 #You can also change this value to a number greater than 2.  I recommend 5 or 7 for scale
    verbose = True #You can also change this value between True and False


    #########################################################################################################

    #The absurd mode automatically sets up a worst-case scenario game (feel free to change total_boxes)
    if player_mode == "absurd":
        puzzle = Cat_Puzzle(mode='A', total_boxes=total_boxes, verbose=verbose)

    #The debug mode will allow for a play-by-play analysis of what's happening in absurd mode.  
    #Consider having verbose=True as well to more fully utilize it
    elif player_mode == "debug":
        puzzle = Cat_Puzzle(mode='A', total_boxes=total_boxes, debug=True, verbose=verbose)
        game_not_solved = True
        while game_not_solved:
            game_not_solved = puzzle.take_turn()
            if verbose:
                print(puzzle.get_stats())

    #This mode allows you to customize everything from the command-line
    elif player_mode == "custom":
        puzzle = Cat_Puzzle()
