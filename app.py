from flask import Flask, render_template
from flask_cors import CORS
from api import api
from db import initDB

app = Flask(__name__)
app.config.from_pyfile('app.cfg')
CORS(app)
initDB(app)
app.register_blueprint(api)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()