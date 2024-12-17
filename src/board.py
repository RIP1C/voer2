class Board:
    """A data type representing a Connect-4 board
       with an arbitrary number of rows and columns.
    """

    def __init__(self, width, height):
        """Construct objects of type Board, with the given width and height."""
        self.width = width
        self.height = height
        self.data = [[' ']*width for row in range(height)]

        # We hoeven niets terug te geven vanuit een constructor!

    def __repr__(self):
        """This method returns a string representation
           for an object of type Board.
        """
        s = ''                          # de string om terug te geven
        for row in range(0, self.height):
            s += '|'
            for col in range(0, self.width):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2*self.width + 1) * '-'   # onderkant van het bord

        # hier moeten de nummers nog onder gezet worden

        return s       # het bord is compleet, geef het terug

        # TODO: Nelson
    def add_move(self, col, ox):
        pass

        # TODO: Bas
    def clear(self):
        self.data = [[' ']*self.width for row in range(self.height)]

        # TODO: Ronald
    def set_board(self, move_string):
        pass

        # TODO: Demian
    def allows_move(self, col) -> bool:
        pass

        # TODO: Ronald
    def is_full(self) -> bool:
        return True

        # TODO: Demian
    def del_move(self, col):
        pass

        # TODO: Nelson
    def wins_for(self, ox) -> str:
        pass

        # TODO: Bas
    def host_game(self):
        pass

    # blub