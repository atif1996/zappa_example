
from flask import Flask
app = Flask(__name__)

@app.route('/helloworld')
def hello_world():
	return '{"hello" : "world"}', 200;

@app.route('/')
def hello_root():
	return '{"hello" : "root"}', 200;


if __name__ == '__main__':
	print(hello_world());
