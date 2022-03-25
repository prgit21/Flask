from flask import Flask
import datetime
app = Flask(__name__)
@app.route('/date')
def hello_world():
    toRet=datetime.datetime.now()
    return str(toRet)
    