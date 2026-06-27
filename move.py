class Move:
    
    def __init__(self, board):
        self.board = board
        self.selected_piece = None
        self.piece_position = None 



    def move_piece(self, row, col):

        if self.selected_piece is None:

            self.selected_piece = self.board.board[row][col]

            self.piece_position = (row, col)


        else:

            new_position = (row, col)

            self.board.board[self.piece_position[0]][self.piece_position[1]] = "--"

            self.board.board[new_position[0]][new_position[1]] = self.selected_piece

            self.selected_piece = None 
            self.piece_position = None         


