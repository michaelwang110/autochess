from src.PieceManager import PieceManager

class BoardSystem(object):
    def __init__(self):
        self._piece_manager = PieceManager()
    
    def reset_board(self):
        del self._piece_manager
        self._piece_manager = PieceManager()
