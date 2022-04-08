#!/usr/bin/env python3

from random import choice

#This class contains the functionality necessary to try one's hand at the Microsoft/Google interview Cat Puzzle!
#The puzzle is simple.  There is a cat who loves boxes, and you, as the player, get a prize for picking the box with the cat in it.
#However, each day, the cat will move to an adjacent box, and the owner only lets you pick one box per day, charging a small toll for each attempt.
#What strategies can you use to find the cat and win the prize in the fewest number of days, and minimize the overall toll?
#Normal mode lets you play the game normally, Absurd mode will take the form of the worst-case scenario.
class Cat_Puzzle:
    def __init__(self, mode="", total_boxes=0, debug=False, verbose=True):
        self.__mode = self.__get_game_mode(mode)
        if self.__mode in ['N', 'A']:
            self.__verbose = verbose if type(verbose) == bool else True
            self.__total_boxes = self.__get_total_boxes(total_boxes)
            self.__prepare_game()
            if self.__verbose:
                print(f"There are {self.__total_boxes} boxes, the cat is in one of them.  Best of luck!")
                if debug:
                    print(f"(The projected solution should consistently take {2 * self.__total_boxes - 4} turns)")
            if not debug:
                self.__start_game()

    #Ask the user which game mode they would like if not valid or provided. 'N', 'A', and 'E' are accepted
    def __get_game_mode(self, mode):
        while mode not in ['N','A','E']:
            mode = input("What would you like to do?  Enter a corresponding character:\nN (Normal), A (Absurd), E (Exit)\n").upper()
        return mode

    #Ask the user how many boxes they want if not valid or provided.  An integer > 2 is accepted
    def __get_total_boxes(self, total_boxes):
        while not self.__acceptable(total_boxes, min_num=2):
            total_boxes = input("How many total_boxes do you want? (Enter an integer greater than 2) \n")
        return int(total_boxes)

    #Ask the user which box they think the cat is in
    def __get_guessed_box(self):
        guessed_box = 0
        self.__guess_count += 1
        while not self.__acceptable(guessed_box, max_num=self.__total_boxes):
            guessed_box = input(f"\nDay #{self.__guess_count}\nWhich box is the cat in?  " \
                    f"(Enter an integer from 1 to {self.__total_boxes})\n")
        return int(guessed_box)

    #Determine if number provided (guessed_box or total_boxes) checks out
    def __acceptable(self, num, min_num=0, max_num=0):
        try:
            if int(num) > min_num:
                if max_num == 0:
                    return True
                elif max_num != 0 and int(num) <= max_num:
                    return True
        except TypeError:
            pass
        except ValueError:
            pass
        return False

    #If we're playing, setup our total_boxes, positions, etc.
    def __prepare_game(self):
        self.__guess_count = 0
        self.__game_not_solved = True
        self.__cat_positions = []
        self.__potential_cat_choices = []
        self.__player_guesses = []
        self.__possible_cat_positions = list(range(1, self.__total_boxes + 1))
        self.__cat_position = choice(self.__possible_cat_positions)
        self.__cat_positions.append(self.__cat_position)

    #Start the game
    def __start_game(self):
        while self.__game_not_solved:
            self.take_turn()
        if self.__verbose:
            print(f"Nicely done!  You found the cat in box #{self.__cat_position}!\n{self.get_stats()}")

    #An accessible function for any machine learning desires, algorithmic check-ins, etc.
    #You can use this function's outputs to help determine a one-fits-all strategy if necessary
    #Facilitates a single guess and assessment
    def take_turn(self):
        guessed_box = self.__get_guessed_box()
        self.__player_guesses.append(guessed_box)
        if guessed_box == self.__cat_position:
            if self.__mode == 'N' or len(self.__potential_cat_choices) == 1:
                self.__game_not_solved = False
            else: #In absurd mode, the cat may move to an adjacent box that was previously feasible if not cornered
                self.__switch_move(guessed_box)
                self.__move_cat()
        else:
            self.__move_cat()
        return self.__game_not_solved

    #Get the possible moves for our cat
    def __get_cat_choices(self):
        move_options = []
        if self.__cat_position > 1:
            move_options.append(self.__cat_position - 1)
        if self.__cat_position < self.__total_boxes:
            move_options.append(self.__cat_position + 1)
        return move_options

    #In Absurd mode, the cat can 'cheat' and move to the other adjacent box if it isn't completely cornered
    #e.g. If the cat supposedly moves from box #3 to #4, and we guess #4, the cat actually is in box #2
    def __switch_move(self, guessed_box):
        if len(self.__potential_cat_choices) == 0: #If this was turn #1, just pick another number
            while self.__cat_position == guessed_box:
                self.__cat_position = choice(self.__possible_cat_positions)
        else:
            other_move_index = (self.__potential_cat_choices.index(self.__cat_position) - 1) * -1
            self.__cat_position = self.__potential_cat_choices[other_move_index]
        self.__cat_positions[len(self.__cat_positions) - 1] = self.__cat_position

    #This function moves the cat to an adjacent box for the upcoming turn
    def __move_cat(self):
        failure_message_intros = [
                "You hear a faint meow from another box.", 
                "You hear some scratching coming from another box.", 
                "You hear a distant 'purr'.", 
                "No cat here.", 
                "You find naught but an open, empty box."
                ]
        failure_message_outros = [
                "The cat moves to an adjacent box while you're gone..",
                "The owner bids you to come back tomorrow..",
                "You'll have to try again tomorrow..",
                "You feel like you're getting closer with each day.."
                ]
        if self.__verbose:
            print(f"{choice(failure_message_intros)}  {choice(failure_message_outros)}")
        self.__potential_cat_choices = self.__get_cat_choices()
        self.__cat_position = choice(self.__potential_cat_choices)
        self.__cat_positions.append(self.__cat_position)

    #An accessible function for any machine learning desires, algorithmic check-ins, etc.
    #You can use this function's outputs to help determine a one-fits-all strategy if necessary
    def get_stats(self):
        return f"Stats:\n  Turns: {self.__guess_count}\n  " \
        f"Cat Positions: {self.__cat_positions}\n  Your Guesses:\t {self.__player_guesses}"
