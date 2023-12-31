import json
import classes

from flask import Flask, request, render_template

app = Flask(__name__)
govno = classes.Govno()
logger = classes.Logger('govnoDB')

@app.route('/')
def to_the_server():
     return render_template('connect.html')


@app.route('/get_jopa')
def get_jopa():
    return {}

@app.route('/load_govno')
def load_govno():
    govno.connect(request)
    logger.insert_govno(int(govno.n_1), 'n_1')
    logger.insert_govno(int(govno.n_2), 'n_2')
    return {}

@app.route('/get_govno')
def get_govno():
    return govno.get_value()

@app.route('/get_chart')
def connect_chart():
    response = logger.govno_chart('n_1')
    return json.dumps(response)


@app.route('/govno1')
def connect_to_govno1():
    return render_template('govno1.html')


@app.route('/govno2')
def connect_to_govno2():
    return render_template('govno2.html')


if __name__ == '__main__':
    app.run()