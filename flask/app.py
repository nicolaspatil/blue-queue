from flask import Flask

app = Flask(__name__)

@app.route('/queue')
def get_queue():
    return {}