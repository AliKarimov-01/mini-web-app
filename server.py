from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('', 'index.html')

@app.route('/script.js')
def script():
    return send_from_directory('', 'script.js')

@app.route('/style.css')
def style():
    return send_from_directory('', 'style.css')

app.run(port=8000)
