from flask import Flask, render_template

app = Flask(__name__)

@app.route('/static/<path:path>')
def static_serve(path):
	return app.send_static_file(os.path.join('static', path))

@app.route('/')
def home():
	return render_template('Yikai Wang.html')

if __name__ == '__main__':
	app.run(debug=True)
