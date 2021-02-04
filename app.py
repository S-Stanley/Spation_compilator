from flask import Flask, jsonify, request
from utils import Files

app = Flask(__name__)

@app.route('/')
def home():
	return (jsonify(True))

@app.route('/python3', methods=['POST'])
def python3():
	try:
		f = request.files['file']
		filename = Files.create_file(str(f.filename), str(f.read()))
		if not filename:
			raise Exception('Erreur de notre coté, veuillez réessayer')
		Files.emulate(filename)
		verif = Files.verif()
		if not verif['res']:
			raise Exception(verif['msg'])
		Files.clean()
		return (jsonify(True))
	except Exception as e:
		print(e)
		print('Error #00004')
		Files.clean()
		return (jsonify(res=False, msg=str(e)))