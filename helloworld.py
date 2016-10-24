
from flask import Flask
import json
app = Flask(__name__)

@app.route('/helloworld')
def hello_world():
    result = dict(hello='world')
    return json.dumps(result), 200;

@app.route('/')
def hello_root():
    result = dict(hello='root')
    return json.dumps(result), 200;


if __name__ == '__main__':
    (message, code) = hello_world()
    print(message)

