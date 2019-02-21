from flask import Flask
from models.BoardSystem import BoardSystem


app = Flask(__name__)


# Board setup
system = BoardSystem()
