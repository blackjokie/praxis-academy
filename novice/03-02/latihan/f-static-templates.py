from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/hello/')

@app.route('/hello/<name>')
def hello(name=None):
    return render_template('index.html', name=name)