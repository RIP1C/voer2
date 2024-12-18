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

class Board():
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

        s += (2*self.width + 1) * '-' + '\n'  # onderkant van het bord

        for col in range(0, self.width):
            s += '|'
            s += str(col)

        # hier moeten de nummers nog onder gezet worden
        s += '|' + '\n'
        return s       # het bord is compleet, geef het terug

    def add_move(self, col: int, ox: str):
        col = int(col)
        for row in range(self.height - 1, -1, -1 ):
            if self.data[row][col] == ' ':
                self.data[row][col] = ox
                break

    def clear(self):
        self.data = [[' ']*self.width for row in range(self.height)]

    def set_board(self, move_string):
        """Accepts a string of columns and places
        alternating checkers in those columns,
        starting with 'X'.

        For example, call b.set_board('012345')
        to see 'X's and 'O's alternate on the
        bottom row, or b.set_board('000000') to
        see them alternate in the left column.

        move_string must be a string of one-digit integers.
        """
        next_checker = 'X'   # we starten door een 'X' te spelen
        for col_char in move_string:
            col = int(col_char)
            if 0 <= col <= self.width:
                self.add_move(col, next_checker)
            
            if next_checker == 'X':
                next_checker = 'O'
            else:
                next_checker = 'X'

    def allows_move(self, col) -> bool:
        col = int(col)
        if col < 0 or col >= self.width:
            return False
        for row in range(self.height):
            if self.data[row][col] == ' ':
                return True
        return False
                
    def is_full(self) -> bool:
        counter = 0
        for col in self.data[0]:
            if col != ' ':
                counter += 1
            if counter >= self.width:
                return True
        return False

    def del_move(self, col):
        col = int(col)
        if col < 0 or col >= self.width:
            return
        for row in range(self.height):
            if self.data[row][col] != ' ':
                self.data[row][col] = ' '
                return
            
    def wins_for(self, ox) -> bool:
        for row in range(self.height):
            for col in range(self.width):
                if in_a_row_n_east(ox, row, col, self.data, 4) or in_a_row_n_northeast(ox, row, col, self.data, 4) or in_a_row_n_south(ox, row, col, self.data, 4) or in_a_row_n_southeast(ox, row, col, self.data, 4):
                    return True
        else: 
            return False
        
    def cols_to_win(self, ox):
        
        ai = []
        if self.allows_move() == True:
            return self.add_move()
        if self.wins_for() == True:
            ai += col


    def ai_move(self, ox):     
        pass

    def host_game(self):
        
        running = True
        current_player = 'X'
        old_player = 'O'

        while running:
            print(f"\n{self}")
            inp = input(f'Keuze van {current_player}: ')

            # Check of inp een integer is
            try:
                int(inp)
            except ValueError:
                print(f"Speler, '{current_player}', {inp} is geen integer!")
                continue

            # Checked of wat de speler doet wel mag
            if not self.allows_move(inp):
                print(f"Speler, '{current_player}', dat mag niet!")
                continue
            
            # Add move
            self.add_move(inp, current_player)

            # Check of dat de winnende move was of bord vol is
            if self.wins_for(current_player) or self.is_full():
                if self.is_full():
                    print(f"Bord is vol -- Niemand heeft gewonnen!")
                else:
                    print(f"{current_player} wint -- Gefeliciteerd!")
                running = False
            
            # Einde ronde, wissel van speler
            (current_player, old_player) = (old_player, current_player)

