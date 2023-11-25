""" Module server   """
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    """_summary_

    Returns:
        _type_: string
    """
    return "<p>Hello, World!</p>"
