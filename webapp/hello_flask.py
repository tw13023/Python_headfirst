from flask import Flask
from vsearch import search4letters
app = Flask(__name__)

@app.route("/")
def hello_world() -> str:
    return "Hello world from Flask!"
@app.route("/search4")
def do_search():
    return str(search4letters('life,the universe,and everything', 'eiru,!'))