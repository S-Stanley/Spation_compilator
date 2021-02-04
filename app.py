from flask import Flask, jsonify, request
from utils import files

app = Flask(__name__)

@app.route('/')
def home():
	return (jsonify(True))

@app.route('/python3', methods=['POST'])
def python3():
	try:
		f = request.files['file']
		filename = files.create_file(str(f.filename), str(f.read()))
		if not filename:
			raise Exception('Erreur de notre coté, veuillez réessayer')
		files.emulate(filename)
		verif = files.verif()
		if not verif['res']:
			raise Exception(verif['msg'])
		files.clean()
		return (jsonify(True))
	except Exception as e:
		print(e)
		print('Error #00004')
		files.clean()
		return (jsonify(res=False, msg=str(e)))