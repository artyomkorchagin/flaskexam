import json
import classes

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def to_the_server():
     return {} # render_template('connect.html')


if __name__ == '__main__':
    app.run()