from src.PieceManager import PieceManager

class BoardSystem(object):
    def __init__(self):
        self.piece_manager = PieceManager()
    
    def pieces_on_board(self):
        list_of_pieces = []
        for piece, count in self.piece_manager._pieces:
            if count != 0:
                list_of_pieces.append(piece)
        return list_of_pieces
    
    def add_piece(self, piece):
        self.piece_manager.add_piece(piece)
    
    def remove_piece(self, piece):
        self.piece_manager.remove_piece(piece)

    def reset_board(self):
        self.piece_manager.set_pieces_to_zero()

#    def get_synergy(self):