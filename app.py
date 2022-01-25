from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
	return 'I am Mariraja CEO of iWEB TEZ..'
if __name__ == '__main__':
	app.run()






