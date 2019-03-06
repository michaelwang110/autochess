from server import app, system
from flask import redirect, request, render_template, url_for, abort


@app.route('/', methods=['GET', 'POST'])
def home():
    return(render_template('home.html'))