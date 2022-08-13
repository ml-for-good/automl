from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app,  resources={r"/*": {"origins": "*"}})

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8030, debug=True)