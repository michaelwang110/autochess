# Stores a dictionary with Pieces key and Counter value
class PieceManager(object):
    def __init__(self):
        self._pieces = {}

    def add_piece(self, piece):
        if piece in self._pieces:
            self._pieces[piece] += 1
        else:
            self._pieces[piece] = 0
    
    def remove_piece(self, piece):
        if self._pieces[piece] != 0:
            self._pieces[piece] -= 1

    def display(self):
        return self._pieces
