def in_a_row_n_east(ch, r_start, c_start, a, n):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists a (array),
       returns True if there are n ch's in a row
       heading east and returns False otherwise.
    """
    h = len(a)
    w = len(a[0])
    if r_start < 0 or r_start > h - 1:
        return False  # rij buiten de grenzen
    if c_start < 0 or c_start + (n-1) > w - 1:
        return False  # kolom buiten de grenzen
    # lus over elke _offset_ i van de locatie
    for i in range(n):
        if a[r_start][c_start+i] != ch:  # klopt niet!
            return False
    return True  # alle offsets kloppen, dus we geven True terug


def in_a_row_n_south(ch, r_start, c_start, a, n):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists a (array),
       returns True if there are n ch's in a row
       heading south and returns False otherwise.
    """
    h = len(a)
    w = len(a[0])
    if r_start < 0 or r_start + (n-1) > h - 1:
        return False  # rij buiten de grenzen
    if c_start < 0 or c_start > w - 1:
        return False  # kolom buiten de grenzen
    # lus over elke _offset_ i van de locatie
    for i in range(n):
        if a[r_start+i][c_start] != ch:  # klopt niet!
            return False
    return True  # alle offsets kloppen, dus we geven True terug


def in_a_row_n_northeast(ch, r_start, c_start, a, n):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists a (array),
       returns True if there are n ch's in a row
       heading northeast and returns False otherwise.
    """
    h = len(a)
    w = len(a[0])
    if r_start - (n-1) < 0 or r_start > h - 1:
        return False  # rij buiten de grenzen
    if c_start < 0 or c_start + (n-1) > w - 1:
        return False  # kolom buiten de grenzen
    # lus over elke _offset_ i van de locatie
    for i in range(n):
        if a[r_start-i][c_start+i] != ch:  # klopt niet!
            return False
    return True  # alle offsets kloppen, dus we geven True terug


def in_a_row_n_southeast(ch, r_start, c_start, a, n):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists a (array),
       returns True if there are n ch's in a row
       heading southeast and returns False otherwise.
    """
    h = len(a)
    w = len(a[0])
    if r_start < 0 or r_start + (n-1) > h - 1:
        return False  # rij buiten de grenzen
    if c_start < 0 or c_start + (n-1) > w - 1:
        return False  # kolom buiten de grenzen
    # lus over elke _offset_ i van de locatie
    for i in range(n):
        if a[r_start+i][c_start+i] != ch:  # klopt niet!
            return False
    return True  # alle offsets kloppen, dus we geven True terug

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
        
        for row in range(self.height - 1, -1, -1 ):
            if self.data[row][col] == ' ' :
                self.data[row][col] = ox
                break


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
    def wins_for(self, ox) -> bool:
        for row in range(self.height):
            for col in range(self.width):
                if in_a_row_n_east(ox, row, col, self.data, 4) or in_a_row_n_northeast(ox, row, col, self.data, 4) or in_a_row_n_south(ox, row, col, self.data, 4) or in_a_row_n_southeast(ox, row, col, self.data, 4):
                    return True
        else: 
            return False
        

        # TODO: Bas
    def host_game(self):
        pass

    #   blub