from unicodedata import name
from flask import Flask,render_template
import datetime


app = Flask(__name__)
@app.route('/')
def hello_world():
    toRet=datetime.datetime.now()
    name='pranav'
    return render_template('index.html', name=name)

