# Author: Kevin Hoang
# GitHub username: GitKevinH
# Date: 08/15/2024
# Description: Portfolio Project - Pentago Game!



class Pentago():
    """
    Class to represent the boardgame Pentago
    """
    def __init__(self):
        """
        Inializes Pentago game instance with default values: game_state, game_dictionary (to hold key:values for coordinates), and player_turn datamembers 

        """
        self._gamestate = "UNFINISHED"
        self._game_dictionary = self.create_dict()
        self._player_turn = "black"

    def get_game_dictionary(self):
        """
        Returns game dictionary where move memory is stored
        """
        return self._game_dictionary

    def create_dict(self):
        """
        Helper function to fill game dictionary with keys
        """
        game_dict = {}
        num_set  = [0,1,2,3,4,5]
        char_set = ['a','b','c','d','e','f']

        for char in char_set:
            for num in num_set:
                game_dict[char+str(num)] = 'none'

        return game_dict
    
    def get_quadrant(self, requested_quadrant):
        """
        Function that returns a dictionary of coordinates for a specific quadrant of the game board
        """
        game_dict = self.get_game_dictionary()
        quad_dict = {}
        quad_list = []

        quadrant_one_char = ['a','b','c']
        quadrant_one_num = [0,1,2]

        quadrant_two_char = ['a','b','c']
        quadrant_two_num = [3,4,5]    

        quadrant_three_char = ['d','e','f']
        quadrant_three_num = [0,1,2]
    
        quadrant_four_char = ['d','e','f']
        quadrant_four_num = [3,4,5]
        
        if requested_quadrant == 1:
            selected_quadrant_char = quadrant_one_char
            selected_quadrant_num = quadrant_one_num
        elif requested_quadrant == 2:
            selected_quadrant_char = quadrant_two_char
            selected_quadrant_num = quadrant_two_num     
        elif requested_quadrant == 3:
            selected_quadrant_char = quadrant_three_char
            selected_quadrant_num = quadrant_three_num 
        elif requested_quadrant == 4:
            selected_quadrant_char = quadrant_four_char
            selected_quadrant_num = quadrant_four_num 

        for char in selected_quadrant_char:
            for num in selected_quadrant_num:
                quad_dict[char+str(num)] = game_dict[char+str(num)]

        return quad_dict


    def get_game_state(self):
        """
        Returns game state - UNFINISHED, WHITE_WON, bLACK_WON, DRAW - which is set via check_win_condition method.
        """
        return self._gamestate
    
    def set_game_state(self, state):
        """
        Setter for changing the state of the game
        """
        self._gamestate = state

    def is_board_full(self):
        """
        Returns True or False checking if board is full by iterating through the dictionary data member that holds the board values
        """
        return all([value == "none" for value in self.get_game_dictionary().values()])
    
    def get_player_turn(self):
        """
        Returns player turn data member
        """
        return self._player_turn
    
    def set_player_turn(self, player):
        """
        Sets player turn
        """
        self._player_turn = player

    def next_turn(self):
        """
        Function flips player turn when called
        """
        if self.get_player_turn() == 'black':
            self.set_player_turn("white")
        else: self.set_player_turn("black")

    

    def make_move(self, color, position, sub_board, rotation):
        """
        Function that contains logic of the desired player move by 
        getting position key in dictionary, checking then setting value from key, then selecting a group of keys (sub-board) to be rotated via rotate() method
        """
        game_dict = self.get_game_dictionary()

        if self.get_player_turn() == color and self.valid_move(position):

            game_dict[position] = color

            self.check_win_condition()
            if self.get_game_state() == "BLACK_WON" or self.get_game_state() == "WHITE_WON" or self.get_game_state() == "DRAW":
                return "game is finished"
            
            self.rotate(sub_board, rotation)

            self.check_win_condition()
            if self.get_game_state() == "BLACK_WON" or self.get_game_state() == "WHITE_WON" or self.get_game_state() == "DRAW":
                return "game is finished"
            
            self.next_turn()
            return True
        else:
            if self.get_player_turn() != color:
                return "not this player's turn"

            if self.valid_move(position) != True:
                return "position is not empty"
        
        # if self.get_game_state() == "BLACK_WON" or self.get_game_state() == "WHITE_WON" or self.get_game_state() == "DRAW":
        #     return "game is finished"
        # else: return True



    def print_board(self):
        """
        Prints board out to console by iterating through dictionary and printing out 6 rows in sequences of 6 values of the game dictionary, ending with newline characters.
        """
        game_dict = list(self.get_game_dictionary().values())
        
        for index in range(len(game_dict)):
            if game_dict[index] == "black":
                print('○', end='   ')
            elif game_dict[index] == "white":
                print('●', end='   ') 
            elif game_dict[index] == 'none':
                print('x', end='   ')
            if (index + 1) % 6 == 0:
                print('\n')


    def valid_move(self, coordinate):
        """
        Function to check value of the key in the dictionary to see if it's black or white or none. If none then true will be returned, false if otherwise
        """
        if self.get_game_dictionary()[coordinate] != "none":
            return False
        return True

    def check_win_condition(self):
        """
        function will check for rows for 5 of the same color, columns for 5 of the same color, and hard coded checks for the possible combinations of diagonal sequences of 5 of the same color, returning the value of the color that has met the win condition if any. 
        function will have conditions set if both colors happen to have 5 sequences at the same time, and return draw.
        """
        game_dict = self.get_game_dictionary()

        #Not proud of how I approached this but it's getting late and my brain is mush. Will come back in the future to clean this up and iterate the game_dict keys somehow.
        #Row wins
        win_condition = [
                        [game_dict['a0'], game_dict['a1'], game_dict['a2'], game_dict['a3'], game_dict['a4']],
                        [game_dict['a1'], game_dict['a2'], game_dict['a3'], game_dict['a4'], game_dict['a5']],
                        [game_dict['b0'], game_dict['b1'], game_dict['b2'], game_dict['b3'], game_dict['b4']],
                        [game_dict['b1'], game_dict['b2'], game_dict['b3'], game_dict['b4'], game_dict['b5']],
                        [game_dict['c0'], game_dict['c1'], game_dict['c2'], game_dict['c3'], game_dict['c4']],
                        [game_dict['c1'], game_dict['c2'], game_dict['c3'], game_dict['c4'], game_dict['c5']],
                        [game_dict['d0'], game_dict['d1'], game_dict['d2'], game_dict['d3'], game_dict['d4']],
                        [game_dict['d1'], game_dict['d2'], game_dict['d3'], game_dict['d4'], game_dict['d5']],
                        [game_dict['e0'], game_dict['e1'], game_dict['e2'], game_dict['e3'], game_dict['e4']],
                        [game_dict['e1'], game_dict['e2'], game_dict['e3'], game_dict['e4'], game_dict['e5']],
                        [game_dict['f0'], game_dict['f1'], game_dict['f2'], game_dict['f3'], game_dict['f4']],
                        [game_dict['f1'], game_dict['f2'], game_dict['f3'], game_dict['f4'], game_dict['f5']],
                        [game_dict['a0'], game_dict['b0'], game_dict['c0'], game_dict['d0'], game_dict['e0']],
                        [game_dict['b0'], game_dict['c0'], game_dict['d0'], game_dict['e0'], game_dict['f0']],
                        [game_dict['a1'], game_dict['b1'], game_dict['c1'], game_dict['d1'], game_dict['e1']],
                        [game_dict['b1'], game_dict['c1'], game_dict['d1'], game_dict['e1'], game_dict['f1']],
                        [game_dict['a2'], game_dict['b2'], game_dict['c2'], game_dict['d2'], game_dict['e2']],
                        [game_dict['b2'], game_dict['c2'], game_dict['d2'], game_dict['e2'], game_dict['f2']],
                        [game_dict['a3'], game_dict['b3'], game_dict['c3'], game_dict['d3'], game_dict['e3']],
                        [game_dict['b3'], game_dict['c3'], game_dict['d3'], game_dict['e3'], game_dict['f3']],
                        [game_dict['a4'], game_dict['b4'], game_dict['c4'], game_dict['d4'], game_dict['e4']],
                        [game_dict['b4'], game_dict['c4'], game_dict['d4'], game_dict['e4'], game_dict['f4']],
                        [game_dict['a5'], game_dict['b5'], game_dict['c5'], game_dict['d5'], game_dict['e5']],
                        [game_dict['b5'], game_dict['c5'], game_dict['d5'], game_dict['e5'], game_dict['f5']],
                        [game_dict['a0'], game_dict['b1'], game_dict['c2'], game_dict['d3'], game_dict['e4']],
                        [game_dict['b1'], game_dict['c2'], game_dict['d3'], game_dict['e4'], game_dict['f5']],
                        [game_dict['f0'], game_dict['e1'], game_dict['d2'], game_dict['c3'], game_dict['b4']],
                        [game_dict['e1'], game_dict['d2'], game_dict['c3'], game_dict['b4'], game_dict['a5']],
                        [game_dict['b0'], game_dict['c1'], game_dict['d2'], game_dict['e3'], game_dict['f4']],
                        [game_dict['a1'], game_dict['b2'], game_dict['c3'], game_dict['d4'], game_dict['e5']],
                        [game_dict['e0'], game_dict['d1'], game_dict['c2'], game_dict['b3'], game_dict['a4']],
                        [game_dict['f1'], game_dict['e2'], game_dict['d3'], game_dict['c4'], game_dict['b5']]
                        ]

        # #Row wins
        # win_cond = [game_dict['a0'], game_dict['a1'], game_dict['a2'], game_dict['a3'], game_dict['a4']]
        # win_cond = [game_dict['a1'], game_dict['a2'], game_dict['a3'], game_dict['a4'], game_dict['a5']]

        # win_cond = [game_dict['b0'], game_dict['b1'], game_dict['b2'], game_dict['b3'], game_dict['b4']]
        # win_cond = [game_dict['b1'], game_dict['b2'], game_dict['b3'], game_dict['b4'], game_dict['b5']]
        
        # win_cond = [game_dict['c0'], game_dict['c1'], game_dict['c2'], game_dict['c3'], game_dict['c4']]
        # win_cond = [game_dict['c1'], game_dict['c2'], game_dict['c3'], game_dict['c4'], game_dict['c5']]

        # win_cond = [game_dict['d0'], game_dict['d1'], game_dict['d2'], game_dict['d3'], game_dict['d4']]
        # win_cond = [game_dict['d1'], game_dict['d2'], game_dict['d3'], game_dict['d4'], game_dict['d5']]

        # win_cond = [game_dict['e0'], game_dict['e1'], game_dict['e2'], game_dict['e3'], game_dict['e4']]
        # win_cond = [game_dict['e1'], game_dict['e2'], game_dict['e3'], game_dict['e4'], game_dict['e5']]

        # win_cond = [game_dict['f0'], game_dict['f1'], game_dict['f2'], game_dict['f3'], game_dict['f4']]
        # win_cond = [game_dict['f1'], game_dict['f2'], game_dict['f3'], game_dict['f4'], game_dict['f5']]

        # #Column wins
        # win_cond = [game_dict['a0'], game_dict['b0'], game_dict['c0'], game_dict['d0'], game_dict['e0']]
        # win_cond = [game_dict['b0'], game_dict['c0'], game_dict['d0'], game_dict['e0'], game_dict['f0']]

        # win_cond = [game_dict['a1'], game_dict['b1'], game_dict['c1'], game_dict['d1'], game_dict['e1']]
        # win_cond = [game_dict['b1'], game_dict['c1'], game_dict['d1'], game_dict['e1'], game_dict['f1']]

        # win_cond = [game_dict['a2'], game_dict['b2'], game_dict['c2'], game_dict['d2'], game_dict['e2']]
        # win_cond = [game_dict['b2'], game_dict['c2'], game_dict['d2'], game_dict['e2'], game_dict['f2']]

        # win_cond = [game_dict['a3'], game_dict['b3'], game_dict['c3'], game_dict['d3'], game_dict['e3']]
        # win_cond = [game_dict['b3'], game_dict['c3'], game_dict['d3'], game_dict['e3'], game_dict['f3']]

        # win_cond = [game_dict['a4'], game_dict['b4'], game_dict['c4'], game_dict['d4'], game_dict['e4']]
        # win_cond = [game_dict['b4'], game_dict['c4'], game_dict['d4'], game_dict['e4'], game_dict['f4']]

        # win_cond = [game_dict['a5'], game_dict['b5'], game_dict['c5'], game_dict['d5'], game_dict['e5']]
        # win_cond = [game_dict['b5'], game_dict['c5'], game_dict['d5'], game_dict['e5'], game_dict['f5']]

        # #Diagonal wins

        # win_cond = [game_dict['a0'], game_dict['b1'], game_dict['c2'], game_dict['d3'], game_dict['e4']]
        # win_cond = [game_dict['b1'], game_dict['c2'], game_dict['d3'], game_dict['e4'], game_dict['f5']]

        # win_cond = [game_dict['f0'], game_dict['e1'], game_dict['d2'], game_dict['c3'], game_dict['b4']]
        # win_cond = [game_dict['e1'], game_dict['d2'], game_dict['c3'], game_dict['b4'], game_dict['a5']]

        # win_cond = [game_dict['b0'], game_dict['c1'], game_dict['d2'], game_dict['e3'], game_dict['f4']]
        # win_cond = [game_dict['a1'], game_dict['b2'], game_dict['c3'], game_dict['d4'], game_dict['e5']]

        # win_cond = [game_dict['e0'], game_dict['d1'], game_dict['c2'], game_dict['b3'], game_dict['a4']]
        # win_cond = [game_dict['f1'], game_dict['e2'], game_dict['d3'], game_dict['c4'], game_dict['b5']]
        
        for winner in win_condition:
            black_won = all(value == 'black' for value in winner)
            if black_won == True:
                break

        for winner in win_condition:
            white_won = all(value == 'white' for value in winner)
            if white_won == True:
                break

        if black_won and white_won:
            #print("Draw")
            self.set_game_state('DRAW')
            
        elif black_won and not white_won:
            #print("Black Won")
            self.set_game_state('BLACK_WON')
            
        elif white_won and not black_won:
            #print("white Won")
            self.set_game_state('WHITE_WON')

        elif self.is_board_full == True:
            self.set_game_state('DRAW')
            

    def rotate(self, quadrant, direction):
        """
        Function will rotate a quadrant by having each quadrant given a set of keys from the dictionary
        and reassigning values based on direction of rotation.
        """
        game_dict = self.get_game_dictionary()
        quadrant_to_rotate = self.get_quadrant(quadrant)
        game_dict_values = list(quadrant_to_rotate.values())
        rotated_quadrant_values = []
        clockwise_rotation =[7,4,1,8,5,2,9,6,3]
        index = 0

        if direction == "C":
            rotation = clockwise_rotation
        elif direction == 'A':
            clockwise_rotation.reverse()
            rotation = clockwise_rotation
        #using clockwise_rotation, we add to rotated_quadrant_values list in order of what coordinate values in sequence of the quadrant_to_rotate's dictionary
        for position in rotation:
            rotated_quadrant_values.append(game_dict_values[position-1])
        #We then assign those values to quadrant_to_rotate's keys
        for values in quadrant_to_rotate:
            quadrant_to_rotate[values] = rotated_quadrant_values[index]
            index += 1
        #Now assign to the game's dictionary
        for count in quadrant_to_rotate:
            game_dict[count] = quadrant_to_rotate[count]
            
                
        
# new_game = Pentago()
# new_game.print_board()
# new_game.check_win_condition()
# print(new_game.get_game_dictionary())

# game = Pentago()
# print(game.make_move('black', 'a2', 1, 'C'))
# print(game.make_move('white', 'a2', 1, 'C'))
# print(game.is_board_full())
# game.print_board()
# print(game.get_game_state())

"""
DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS

1. Initializing the Pentago class
    1. My program will initialize the Pentago class within the main method. The main method will hold the logic (using while True, until the Pentago’s game_state() method returns something other than unfinished then breaks out of loop) that allows the game to continue on until the win condition (or draw condition) is met. 
2. Keeping track of turn order
    1. whos_turn() method will be used to check who’s current turn by returning the data attribute ‘turn’ from the Pentago class.
    2. turn_order() method that takes checks current value of the ‘turn’ data member in the Pentago class and changes between black and white
3. Keeping track of the current board position
    1. board position is a comprised of a large 36 entry dictionary in a large list with the element positions switching within those lists when requested
4. Determining if a regular move is valid
    1. valid_move() method that checks if there is a value other than None for the value of the key (coordinate) found in the dictionary
5. Rotating the sub-board
    1. rotate() method that takes in one of the dictionaries in the larger list and moves the elements according to moving will be done by swapping values from original position to expected position based on counterclockwise or clockwise
6. Updating the board to reflect the valid move
    1. A dictionary will be used with the coordinates holding the key and the values being updated to be ‘black’ or ‘white’
7. Determining whether there is any 5-in-row on the board for one color of the piece
    1. check_win_condition() method will check for rows for 5 of the same color, columns for 5 of the same color, and hard coded checks for the possible combinations of diagonal sequences of 5 of the same color, returning the value of the color that has met the win condition if any. Method will have conditions set if both colors happen to have 5 sequences at the same time, and return draw.
8. Determining whether the current board is full
    1. is_board_full() method will iterate through the dictionary values and check if all of them are not equal to None
9. Determining the current state of the game
    1. get_game_state() will run check_win_condition and if the check_win_condition returns a color or draw, it will set the game state accordingly. It will also call the is_board_full method to see if the game is a draw. Else it will remain in the initial state (unfinished)
10. How to present the board using the print method
    1. print_board method will take in the big list of 4 dictionaries and convert the values found into a single list. The single list will then be iterated through and print out rows with 6 columns with a newline character at the end to show the board in the console.


"""


