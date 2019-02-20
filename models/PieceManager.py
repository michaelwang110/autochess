from Piece import Piece

class PieceManager(object):
    def __init__(self):
        self._pieces = []
    
    def add_piece(self, name, class, species, cost):
        self._pieces.append(Piece(name, class, species, cost)

    def remove_piece(self, name):
        for piece in self._pieces:
            if piece.name == name:
                self._pieces.remove(piece)
                break

    def display(self):
        return self._pieces
