import json
import classes

from flask import Flask, request, render_template

app = Flask(__name__)
linker = classes.text_linker()
@app.route('/')
def to_the_server():
     return render_template('connect.html')

@app.route('/get_jopa')
def penis():
    return {} #linker.connect("323")


if __name__ == '__main__':
    app.run()