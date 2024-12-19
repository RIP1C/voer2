from board import Board

# Hier begint onze programma.
def main(board: Board):
    board.set_board('334050505')
    board.add_move(0, "X")
    
    print(board)
    
    input()
    





main(Board(7, 6)) 




