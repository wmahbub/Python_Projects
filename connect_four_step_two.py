
from connect_four_step_one import Board



# Step 1

class Player:

    def __init__(self, checker):
        """ doc string """
        assert(checker == 'X' or checker == 'O')

        self.checker= checker
        self.num_moves= 0

        
# Step 2

    def __repr__(self):
        """ doc string """
        return 'Player ' + self.checker


# Step 3

    def opponent_checker(self):
        """ doc string """
        if self.checker == 'X':
            return 'O'

        elif self.checker == 'O':
            return 'X'

# Step 4

    def next_move(self, b):
        """ doc string """

        while True:
            col = int(input('Enter a column: '))

            if board.can_add_to(col)== True:
                self.num_moves += 1
                return col

            else:
                print('Try again!')


p = Player('X')
b1 = Board(6, 7)
            
            
                
                
        







        
        
        
