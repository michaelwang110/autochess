from flask import Flask
from src.BoardSystem import BoardSystem


app = Flask(__name__)


# Board setup
system = BoardSystem()
