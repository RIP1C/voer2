from board import Board

# Hier begint onze programma.
def main(board: Board):
    board.host_ai_game()
    
main(Board(7, 6)) 
