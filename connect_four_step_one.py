
# Step 1

class Board:

    def __init__(self, height, width):
        """ doc string """

        self.height = height
        self.width = width
        self.slots = [ [' '] * self.width for row in range(self.height)]


# Step 2

    def __repr__(self):
        """ doc string """

        s = ''
        c = 0

        for row in range(self.height):
            s += '|'

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'

        for dash in range((self.width*2)+1):
            s+= '-'

        s += '\n'

        for col in range(self.width):
            s += ' ' + str(col%10)

        return s


# Step 3

    def add_checker(self, checker, col):
        """ doc string """
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)

        start_height= -1

        if self.slots[start_height][col]== ' ':
            self.slots[start_height][col] = checker

        else:
            for height in range(-1,-self.height-1,-1):
                if self.slots[height][col] == ' ':
                    self.slots[height][col] = checker
                    break

     
# Step 4

    def reset(self):
        """ doc string """
        self.slots = [[' '] * self.width for row in range(self.height)]


# Step 5

    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
            checkers in those columns of the called Board object, 
            starting with 'X'.
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'


# Step 6

    def can_add_to(self, col):
        """ doc string """
        assert(col != '')

        if col<0 or col>= self.width:
            return False

        else:
            if self.slots[-self.height][col] != ' ':
                return False
            else:
                if 0 <= col < self.width:
                    for height in range(-1,-self.height-1,-1):
                        if self.slots[height][col]== ' ':
                            return True
    

# Step 7

    def is_full(self):
        """ doc string """
        for i in range(self.width):
            if self.can_add_to(i)== True:
                return False
        else:
            return True


# Step 8

    def remove_checker(self, col):
        """ doc string """
        for i in range(0,self.height):
            if self.slots[i][col] != ' ':
                self.slots[i][col]= ' '
                break
            else:
                if self.slots[i][col]==' ':
                    self.slots[i][col]=' '

# Step 9

    def is_win_for(self, checker):
        """ doc string """
        assert(checker == 'X' or checker == 'O')

        if self.is_horizontal_win(checker)== True or \
           self.is_vertical_win(checker)== True or \
           self.is_downd_win(checker) == True or \
           self.is_upd_win(checker)== True :

            return True

        else:
            return False


    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker."""
        for row in range(self.height):
            for col in range(self.width - 3):
   
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True

        return False


    def is_vertical_win(self, checker):
        """ Checks for a horizontal win for the specified checker."""
        for row in range(self.height-3):
            for col in range(self.width):
      
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col] == checker and \
                   self.slots[row + 2][col] == checker and \
                   self.slots[row + 3][col] == checker:
                    return True

        return False


    def is_downd_win(self, checker):
        """ Checks for a horizontal win for the specified checker."""
        if self.slots[row]<4:
            return False

        else:

            for row in range(self.height-3):
                for col in range(self.width-3):
      
                    if self.slots[row][col] == checker and \
                       self.slots[row + 1][col + 1] == checker and \
                       self.slots[row + 2][col + 2] == checker and \
                       self.slots[row + 3][col + 3] == checker:
                        return True

            return False

    def is_upd_win(self, checker):
        """ Checks for a horizontal win for the specified checker."""
        if self.slots[row]<4:
            return False

        else:

            for row in range(-1,-self.height-1,-1):
                for col in range(self.width-3):

                    if self.slots[row][col] == checker and \
                       self.slots[row - 1][col + 1] == checker and \
                       self.slots[row - 2][col + 2] == checker and \
                       self.slots[row - 3][col + 3] == checker:
                        return True

            return False

    

# Test Cases
"""
b1= Board(6, 7)
b1.add_checkers('00102030')

b2 = Board(6, 7)
b2.add_checker('X',0 )
b2.add_checker('X',0 )
b2.add_checker('X',0 )
b2.add_checker('O',0 )
b2.add_checker('X',1 )
b2.add_checker('X',1 )
b2.add_checker('O',1 )
b2.add_checker('X',2 )
b2.add_checker('O',2 )
b2.add_checker('O',3 )


b3 = Board(6, 7)
b3.add_checkers('23344545515')
"""
