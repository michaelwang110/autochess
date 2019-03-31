from flask import Flask
from src.BoardSystem import BoardSystem
from src.Piece import Piece
import csv

app = Flask(__name__)
app.secret_key = 'very-secret-123'

# Board setup
board = BoardSystem()

# input Piece details
with open('pieces/pieces.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        name = row[0]
        species = [row[1], None if row[2] == 'None' else row[2]]
        clas = row[3]
        cost = int(row[4])
        tier = int(row[5])
        board.piece_manager.add_piece(Piece(name, species, clas, cost, tier))