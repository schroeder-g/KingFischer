from .Pieces import Piece

class Board:
    def __init__(self):
        self.state: array[array] = [[Square(None, j, i) for j in range(1,9)] for i in range(1, 9)]


    def new_game(self):
        self.state[1] = [Square(Piece("p", "w"), 2, i) for i in range(1, 9)]
        self.state[6] = [Square(Piece("p", "b"), 2, i) for i in range(1, 9)]
        self.state[0] = [Square(Piece("r", "w"), 1, 1), Square(Piece("n", "w"), 2, 1), Square(Piece("b", "w"), 3, 1),
                         Square(Piece("q", "w"), 4, 1), Square(Piece("k", "w"), 5, 1), ]

class Square:
    def __init__(self, piece, row, column):
        self.piece: Piece | None = piece
        self.column: int = column
        self. row: int = row


b = Board()
print(b.state)

# for col in range(len(b.state)):
#     for row in range(len(b.state[0])):
#         print(b.state[col][row].row, b.state[col][row].column)