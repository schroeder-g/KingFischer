class Piece:
    def __init__(self, type, color):
        self.type: "p" | "n" | "b" | "r" | "q" | "k" | None = type
        self.color: "w" | "b" = color

    # def get_possible_moves(self):
