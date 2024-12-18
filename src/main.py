from board import Board

# Hier begint onze programma.
def main(board: Board):
    board.set_board("0000001111112222223333334444445555556666")
    board.add_move(0, "X")
    print(board.is_full())
    print(board)
    input()
    





main(Board(7, 6)) 



