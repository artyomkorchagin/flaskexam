import json
import classes

from flask import Flask, request, render_template

app = Flask(__name__)
linker = classes.text_linker()
govno = classes.Govno()

@app.route('/')
def to_the_server():
     return render_template('connect.html')


@app.route('/get_jopa')
def get_jopa():
    return {} #linker.connect("323")


@app.route('/get_govno')
def get_govno():
    return json.dumps({'n_1': "123", 'n_2': "3213"})

@app.route('/govno1')
def connect_to_govno1():
    return render_template('govno1.html')


@app.route('/govno2')
def connect_to_govno2():
    return render_template('govno2.html')


if __name__ == '__main__':
    app.run()